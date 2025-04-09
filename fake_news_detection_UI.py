import streamlit as st
import pickle

# Load the saved SVM model and vectorizer
with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("!! Fake News Detector !!")
st.subheader("Enter a news article below and find out if it's Fake or Real!")

news_text = st.text_area("🖊️ News Content", height=300, placeholder="Paste the news content here...")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some news content.")
    else:
        input_vector = vectorizer.transform([news_text])
        prediction = model.predict(input_vector)[0]

        if prediction == 0:
            st.success("!! BOOM !! This news is REAL.")
        else:
            st.error("!! OH NOOoooooo!! This news is FAKE.")
