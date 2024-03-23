import re
import math
from collections import Counter

def clean(text):
    cleaned_text = ""
    cleaned_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    cleaned_text = re.sub(r'https?://\S+', '', text) # remove http:// and https://
    cleaned_text = re.sub(r'[\(\)\[\]\{\}]', '', cleaned_text)  # Remove curly brackets and content inside them
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple consecutive spaces with a single space
    cleaned_text = re.sub(r'[.,\*\'\"\!;:-]', '', cleaned_text)
    cleaned_text = cleaned_text.strip().lower()  # Remove leading and trailing spaces
    return cleaned_text

def remove_stopwords(text, stopwords_file):
    with open(stopwords_file, 'r') as stop_file:
        stopwords = stop_file.read().splitlines()

    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)
           
def stemming_and_lemmatization(text):
  preprocessed_text = ""
    
  for word in text.split():
        if word[0].isupper():
            preprocessed_text += word + " "
            continue
        
        modified_word = word
        
        # Apply multiple transformations sequentially
        transformations = [
            (r'ing$', ''),   # Remove 'ing' suffix
            (r'ly$', ''),    # Remove 'ly' suffix
            (r'ment$', '')   # Remove 'ment' suffix
        ]
        
        for pattern, replacement in transformations:
            modified_word = re.sub(pattern, replacement, modified_word)
        
        preprocessed_text += modified_word + " "
    
  return preprocessed_text.strip().lower()
    
def preprocess_texts(documents_file, stopwords_file):
    preprocessed_docs = {}
    with open(documents_file, 'r') as f:
        document_paths = f.readlines()
        document_paths = [path.strip() for path in document_paths]

    for document_path in document_paths:
        with open(document_path, 'r') as infile:
            text = infile.read()

        cleaned_text = clean(text)
        text_no_stopwords = remove_stopwords(cleaned_text, stopwords_file)
        preprocessed_text = stemming_and_lemmatization(text_no_stopwords)

        document_name = document_path.split('/')[-1]

        preprocessed_docs[document_name] = preprocessed_text

    return preprocessed_docs


# ---

def compute_tf_idf(preprocessed_documents):
    tf_idf_results = {}

    # Step 1: Compute TF and IDF for each document
    for doc_name, preprocessed_doc in preprocessed_documents.items():
        # Compute TF
        # print(f"\nComputing TF-IDF for document: {doc_name}")
        term_frequency = Counter(preprocessed_doc.split())
        total_terms = len(preprocessed_doc.split())
        tf = {word: freq/total_terms for word, freq in term_frequency.items()}
        # print(term_frequency)
        # print("TF:", tf)
        
        # Compute IDF
        num_documents = len(preprocessed_documents)
        idf = {}
        # print("total number of documents: ", num_documents)
        
        for word in term_frequency.keys():
          num_docs_with_word = sum(1 for doc in preprocessed_documents.values() if word in doc.split())
          # num_docs_with_word = 0
          # for doc_text in preprocessed_documents.values():
          #     if word in doc_text.split():
          #         num_docs_with_word += 1
          idf[word] = math.log((num_documents) / (num_docs_with_word)) + 1
          # print(word + "-" + " Num of dosc with word: ", num_docs_with_word)

        # print("Number of iterations:", loop_counter) 
        # print("IDF:", idf)
        
        
        # Calculate TF-IDF
        tf_idf_scores = {word: round(tf[word] * idf[word], 2) for word in tf}
        # print("TF-IDF:", tf_idf_scores)
        # Sort and format the results
        sorted_scores = sorted(tf_idf_scores.items(), key=lambda x: (-x[1],x[0]))[:5]
        output_data = [(word, score) for word, score in sorted_scores]
        output_file = "tfidf_" + doc_name
        with open(output_file, 'w') as outfile:
            outfile.write(f"{output_data}")
                
        # Store results in the dictionary
        tf_idf_results[doc_name] = output_data

    return tf_idf_results

# print(preprocessed_docs)
stopwords_file_path = '../data/stopwords.txt'
preprocessed_docs = preprocess_texts('../data/tfidf_docs.txt', stopwords_file_path)
tf_idf_results = compute_tf_idf(preprocessed_docs)
