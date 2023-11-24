import streamlit as st
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Specify NLTK data path
nltk.data.path.append('./nltk_data')

# Download NLTK data
nltk.download('punkt', download_dir='./nltk_data')

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = ngrams(tokens, n)
    return list(n_grams)

# Streamlit UI
def main():
    st.title("N-gram Extractor")

    # User input
    text_input = st.text_area("Enter text:", "Type or paste your text here...")

    # N-gram selection
    n_value = st.slider("Select N for N-grams", min_value=2, max_value=5, value=2)

    # Generate n-grams on button click
    if st.button("Generate N-grams"):
        if text_input:
            st.subheader(f"{n_value}-grams:")
            n_grams = generate_ngrams(text_input, n_value)
            st.write(n_grams)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
