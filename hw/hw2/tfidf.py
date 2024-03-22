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

# ---

def compute_tf_idf(preprocessed_documents):
    tf_idf_results = {}

    # Step 1: Compute TF and IDF for each document
    for doc_name, preprocessed_doc in preprocessed_documents.items():
        # Compute TF
        term_frequency = Counter(preprocessed_doc.split())
        total_terms = len(preprocessed_doc.split())
        tf = {word: freq/total_terms for word, freq in term_frequency.items()}
        
        # Compute IDF
        num_documents = len(preprocessed_documents)
        idf = {}
        for word in term_frequency:
            num_docs_with_word = sum(1 for doc in preprocessed_documents.values() if word in doc)
            idf[word] = math.log(num_documents / num_docs_with_word) + 1

        # Calculate TF-IDF
        tf_idf_scores = {word: round(tf[word] * idf[word], 2) for word in tf}

        # Sort and format the results
        sorted_scores = sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)[:5]
        output_data = [(word, score) for word, score in sorted_scores]
        output_file = "tfidf_" + doc_name
        with open(output_file, 'w') as outfile:
            outfile.write(f"{output_data}")
                
        # Store results in the dictionary
        tf_idf_results[doc_name] = output_data

    return tf_idf_results

preprocessed_docs = preprocess_texts('../data/tfidf_docs.txt')

tf_idf_results = compute_tf_idf(preprocessed_docs)

# Print TF-IDF results
# for doc_name, results in tf_idf_results.items():
#     print(doc_name)
#     for word, score in results:
#         print(f"{word}: {score}")
