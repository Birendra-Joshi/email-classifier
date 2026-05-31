# 📧 Spam Email Classifier

This is a simple Machine Learning project that detects whether an email or message is Spam or Not Spam. I built this project using Python, Scikit-learn, TF-IDF, and Streamlit while learning about Natural Language Processing (NLP) and text classification.

The model analyzes email text and predicts whether the message looks suspicious or safe.

---

# 🚀 Features

* Detects spam and non-spam emails
* Converts text into numerical data using TF-IDF
* Uses Multinomial Naive Bayes for prediction
* Simple Streamlit web interface
* Real-time prediction system
* Trained model saving with Joblib

---

# 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* TF-IDF Vectorizer
* Multinomial Naive Bayes

---

# 📂 Project Structure

```bash id="py4r3e"
spam-classifier/
│
├── app.py
├──requirement.txt
├── train_model.py
├── spam_model.pkl
├── vectorizer.pkl
├── .gitignore
└── README.md
```

---

# 📊 Model Details

* Model Used: Multinomial Naive Bayes
* NLP Technique: TF-IDF Vectorization
* Dataset Size: 192,000 emails
* Classification Type: Spam vs Ham

---

# ⚙️ Installation

Install the required libraries:

```bash id="7l4jvt"
pip install pandas scikit-learn streamlit joblib
```

---

# 🏋️ Training the Model

Run the following command to train the model:

```bash id="jgj8k5"
python train_model.py
```

This will:

* preprocess the dataset
* train the machine learning model
* save the trained model and vectorizer

Generated files:

* `spam_model.pkl`
* `vectorizer.pkl`

---

# 🌐 Running the Web App

Start the Streamlit frontend:

```bash id="xemr3s"
streamlit run app.py
```

The app will automatically open in your browser.

---

# 🧪 Example Messages

## Spam Example

```text id="2hj88x"
Congratulations! You won $5000! Click now!
```

## Normal Example

```text id="ujhrl8"
Can we meet tomorrow at 10am?
```

---

# 📁 Dataset

The dataset file (`emails.csv`) is not included in this repository because of its large size and is added to `.gitignore`.

Download the dataset separately and place it inside the project folder before training the model.

---

# 📌 Future Improvements

Some improvements I would like to add in the future:

* Deep Learning based spam detection
* BERT/Transformer models
* Phishing email detection
* Nepali spam detection
* Better UI/UX
* Smarter email context understanding

---

#  About Me

Birendra Josh
Aspiring Developer from Nepal 🇳🇵

NOTE: THIS PROJECT IS FOR MY MACHINE LEARNING, LEARNING PURPOSES. I AM TRYING TO LEAN AND GROW 

If you like this project, consider giving it a star on GitHub ⭐
