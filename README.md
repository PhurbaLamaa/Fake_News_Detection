# Fake_News_Detection  
A machine learning project to classify fake news using Logistic Regression, Random Forest, and SVM with NLP preprocessing. Includes a Streamlit UI for user input and live predictions.

## 📌 Project Overview
This project aims to detect whether a news article is **real** or **fake** using natural language processing (NLP) and multiple machine learning models. The goal is to provide a streamlined tool with a user interface that allows users to input news text and get an instant prediction.

## 🚀 Features
- Data preprocessing and cleaning using NLP techniques (stopword removal, lemmatization, etc.)
- TF-IDF vectorization for feature extraction
- Training and evaluation of three ML models:
  - Logistic Regression
  - Random Forest Classifier
  - Support Vector Machine (SVM)
- Model comparison using accuracy, confusion matrix, and classification report
- Simple and interactive **Streamlit UI** for live predictions

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Numpy
- NLTK
- Streamlit

## 📂 Dataset
The dataset used contains labeled news articles with a binary label:
- `1`: Fake news
- `0`: Real news

The dataset was preprocessed by:
- Removing punctuation and stopwords
- Converting text to lowercase
- Lemmatization using NLTK
- TF-IDF vectorization to prepare the data for model training

## 📊 Model Evaluation
All three models were evaluated using accuracy scores and classification reports. The Logistic Regression model performed the best with the highest accuracy, making it the final choice for deployment.

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| ~97%     |
| Random Forest      | ~98%     |
| SVM                | ~99%     |

## 🖥️ Streamlit Web App
A simple web interface built with Streamlit allows users to enter a piece of news and get a real-time prediction on whether the news is real or fake.

To run the app locally:
```bash
streamlit run fake_news_detection_UI.py
```
📁 Repository Structure 
├── Fake_real_classifier.ipynb     # Main Jupyter notebook
├── fake_news_detection_UI.py      # Streamlit web app
├── README.md                      # Project documentation
├── requirements.txt               # List of dependencies

📦 Installation
1. Clone the repo:
git clone https://github.com/yourusername/fake_news_detection.git
cd fake_news_detection

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run fake_news_detection_UI.py

📌 Future Improvements
1. Incorporate deep learning models like LSTM or BERT
2. Add more robust preprocessing with named entity recognition
3. Use a larger, more diverse dataset
4.Deploy the app using platforms like Heroku or Streamlit Cloud

🤝 Contributions
Feel free to fork this repo and submit pull requests. All contributions are welcome!

📜 License
This project is open-source and available under the MIT License.
