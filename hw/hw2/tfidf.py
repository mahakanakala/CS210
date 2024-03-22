import re
import math

def clean(text):
    cleaned_text = ""
    cleaned_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    cleaned_text = re.sub(r'https?://\S+', '', text) # remove http:// and https://
    cleaned_text = re.sub(r'[\(\)\[\]\{\}]', '', cleaned_text)  # Remove curly brackets and content inside them
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)  # Replace newline characters with space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple consecutive spaces with a single space
    cleaned_text = re.sub(r'[.,\*\'\";:-]', '', cleaned_text)
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
    # Keep punctuation (periods and apostrophes)
    if word.endswith('.') or word.endswith("'"):
      preprocessed_text += word + " "
      continue
    
    if word[0].isupper():
      preprocessed_text += word + " "
      continue
    
    if word.endswith('ing'):
      word = re.sub(r'ing$', '', word)
    elif word.endswith('ly'):
      word = re.sub(r'ly$', '', word)
    elif word.endswith('ment'):
      word = re.sub(r'ment$', '', word)
    
    preprocessed_text += word + " "
  
  return preprocessed_text.strip().lower()
    
def preprocess_texts(documents_file):
    preprocessed_docs = {}
    with open(documents_file, 'r') as f:
        document_paths = f.readlines()  # Read document paths from file
        document_paths = [path.strip() for path in document_paths]  # Remove trailing newlines

    for document_path in document_paths:
        with open(document_path, 'r') as infile:
         text = infile.read()

        cleaned_text = clean(text)
        text_no_stopwords = remove_stopwords(cleaned_text, '../data/stopwords.txt')
        preprocessed_text = stemming_and_lemmatization(text_no_stopwords)

        # Extract document name from path
        document_name = document_path.split('/')[-1]  # Assuming path format

        # Add preprocessed text to dictionary with document name as key
        preprocessed_docs[document_name] = preprocessed_text

    return preprocessed_docs

preprocessed_docs = preprocess_texts('../data/tfidf_docs.txt')
# preprocess_text('../data/test1.txt')
# preprocess_text('../data/test2.txt')

# ---

def compute_tf_idf(preprocessed_documents):
    tf_idf_results = {}

    # Access preprocessed documents correctly
    for doc_name, preprocessed_doc in preprocessed_documents.items():

        # Step 1: Compute TF
        term_frequency = {}
        total_terms = len(preprocessed_doc.split())  # Split to get individual terms
        for term in preprocessed_doc.split():
            term_frequency[term] = term_frequency.get(term, 0) + 1

        # Step 2: Compute IDF
        document_frequency = {}
        for term in set(preprocessed_doc.split()):  # Split to get unique terms
            for _, other_doc in preprocessed_documents.items():
                if term in other_doc.split():  # Split to compare individual terms
                    document_frequency[term] = document_frequency.get(term, 0) + 1
        num_documents = len(preprocessed_documents)
        inverse_document_frequency = {
            term: math.log(num_documents / (document_frequency[term] + 1)) + 1
            for term in document_frequency
        }

        # Step 3: Calculate TF-IDF
        tf_idf_scores = {
            term: round((term_frequency[term] / total_terms) * inverse_document_frequency[term], 2)
            for term in term_frequency
        }

        # Step 4: Sort and store TF-IDF scores
        sorted_tf_idf = sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_tf_idf[:5]
        tf_idf_results[doc_name] = top_5

        output_file = f"tfidf_{doc_name}"
        with open(output_file, "w") as outfile:
            for word, score in top_5:
                outfile.write(f"{word}: {score}\n")

    return tf_idf_results

# Read and preprocess documents
preprocessed_docs = preprocess_texts('../data/tfidf_docs.txt')

# Compute TF-IDF scores
tf_idf_results = compute_tf_idf(preprocessed_docs)

# Print TF-IDF results
for doc_name, results in tf_idf_results.items():
    print(doc_name)
    for word, score in results:
        print(f"{word}: {score}")

# Read and preprocess documents
# preprocessed_docs = preprocess_texts('../data/tfidf_docs.txt')

# # Compute TF-IDF scores
# tf_idf_results = compute_tf_idf(preprocessed_docs)