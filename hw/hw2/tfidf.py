import re

def clean(text):
    cleaned_text = ""
    cleaned_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)  # Remove square brackets and content inside them
    cleaned_text = re.sub(r'\(.*?\)', '', cleaned_text)  # Remove parentheses and content inside them
    cleaned_text = re.sub(r'\{.*?\}', '', cleaned_text)  # Remove curly brackets and content inside them
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple consecutive spaces with a single space
    cleaned_text = cleaned_text.strip().lower()  # Remove leading and trailing spaces
    return cleaned_text

def remove_stopwords(text, stopwords_file):
    with open(stopwords_file, 'r') as stop_file:
        stopwords = stop_file.read().splitlines()

    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)
           
           
def stemming_and_lemmatization(text):
        stemming_and_lemmatization = ""
        
        for word in text.split():
            if word.endswith('ing'):
                word = re.sub(r'ing$', '', word)
            elif word.endswith('ly'):
                word = re.sub(r'ly$', '', word)
            elif word.endswith('ment'):
                word = re.sub(r'ment$', '', word)
            elif word.endswith('ed'):
                word = re.sub(r'ed$', '', word)
            stemming_and_lemmatization += word + " "
            
        return stemming_and_lemmatization
    
def preprocess_text(input_file, output_file=None):
    if output_file is None:
        file_name = input_file.split("/")[-1].split(".")[0]
        output_file = f'preproc_{file_name}.txt'
        
    with open(input_file, 'r') as infile:
        text = infile.read()
        cleaned_text = clean(text)
        text_no_stopwords = remove_stopwords(cleaned_text, '../data/stopwords.txt')
        preprocessed_text = stemming_and_lemmatization(text_no_stopwords)
    
    with open(output_file, 'w') as outfile:
        outfile.write(preprocessed_text)

preprocess_text('../data/test1.txt')

# ---
import math

def compute_tf_idf(preprocessed_documents):
    tf_idf_results = {}
    for doc_name, preprocessed_doc in preprocessed_documents.items():
        # Step 1: Compute TF
        term_frequency = {}
        total_terms = len(preprocessed_doc)
        for term in preprocessed_doc:
            term_frequency[term] = term_frequency.get(term, 0) + 1
        
        # Step 2: Compute IDF
        document_frequency = {}
        for term in set(preprocessed_doc):
            for _, other_doc in preprocessed_documents.items():
                if term in other_doc:
                    document_frequency[term] = document_frequency.get(term, 0) + 1
        num_documents = len(preprocessed_documents)
        inverse_document_frequency = {term: math.log(num_documents / (document_frequency[term] + 1)) + 1 for term in document_frequency}
        
        # Step 3: Calculate TF-IDF
        tf_idf_scores = {term: (term_frequency[term] / total_terms) * inverse_document_frequency[term] for term in term_frequency}
        
        # Step 4: Sort and store TF-IDF scores
        sorted_tf_idf = sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_tf_idf[:5]
        tf_idf_results[doc_name] = top_5
        
        output_file = f'tfidf_{doc_name}'
        with open(output_file, 'w') as outfile:
            for word, score in top_5:
                outfile.write(f'{word}: {score:.2f}\n')
    
    return tf_idf_results