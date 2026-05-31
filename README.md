# 📧 Spam Email Classifier

Hey there! This is a project I built to detect whether an incoming message or email is Spam or Ham (Not Spam). 

I wanted to dive deeper into Natural Language Processing (NLP) and text classification, so I built this pipeline using Python, Scikit-learn, and Streamlit. The app takes raw text input, runs it through a machine learning model, and spits out a prediction in real-time to let you know if a message looks sketchy or completely safe.

---

###  Live Demo
Want to test it out right now? Try the deployed web app here:
https://email-classifier11.streamlit.app/

---

###  AI Use Declaration
To keep things completely transparent for the hackathon: I used AI assistants (like ChatGPT/Gemini) during development to help me troubleshoot deployment errors on Streamlit Cloud (resolving missing dependencies), fix some layout bugs in the UI, and polish up the project documentation. However, all the core machine learning logic, data handling pipelines, and model choices were built and decided by me.

---

###  Features
* **Real-time Detection:** Paste any text and get an instant prediction.
* **Text Preprocessing:** Converts messy text strings into clean numerical data using a TF-IDF Vectorizer.
* **Fast Inference:** Uses a Multinomial Naive Bayes model for incredibly quick predictions.
* **Clean UI:** A simple, straightforward interface built with Streamlit.
* **Model Persistence:** The trained weights and vectorizers are saved cleanly using Joblib.

###  The Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Machine Learning & NLP:** Scikit-learn (TF-IDF Vectorizer + Multinomial Naive Bayes)
* **Web Framework:** Streamlit
* **Model Saving:** Joblib

###  Project Structure
Here is how the project files are organized:
```text
spam-classifier/
│
├── app.py                # Streamlit web interface
├── requirements.txt      # Production dependencies for cloud deployment
├── train_model.py        # Script to preprocess data and train the model
├── spam_model.pkl        # Saved weights for the trained Naive Bayes model
├── vectorizer.pkl        # Saved vocabulary mapping from TF-IDF
├── .gitignore            # Ignores data files and local virtual envs
└── README.md             # This file right here!
 Model Details & Performance
Algorithm: Multinomial Naive Bayes

Feature Extraction: TF-IDF (Term Frequency-Inverse Document Frequency)

Dataset Size: ~192,000 emails

Task: Binary Classification (0 = Ham, 1 = Spam)

 Model Performance Metrics
When evaluating the model on an unseen test split of 38,770 messages, it achieved an incredible overall accuracy of 96.38%.

Here are the direct training results:

Overall Accuracy: 0.96 (96.38%)

Ham (Safe Emails) Precision: 0.94

Ham (Safe Emails) Recall: 0.99

Spam Precision: 0.99

Spam Recall: 0.93

What these numbers actually mean: > * A 0.99 Spam Precision means that when the model flags an email as spam, it is correct 99% of the time. This ensures almost zero legitimate emails will accidentally end up in the junk folder!

A 0.99 Ham Recall means the model successfully catches and lets through almost every single normal, safe message without blocking it.

 Local Setup Guide
If you want to run this project locally on your machine, just follow these quick steps:

1. Install Dependencies
Make sure you have Python installed, then run:

Bash
pip install pandas scikit-learn streamlit joblib
2. Train the Model
To train the model from scratch and generate your own .pkl files, run:

Bash
python train_model.py
Note: This script will preprocess the dataset, train the Naive Bayes classifier, and save both spam_model.pkl and vectorizer.pkl to your folder.

3. Spin up the Web App
Launch the Streamlit interface locally by running:

Bash
streamlit run app.py
This should automatically open up a window in your default browser at http://localhost:8501.

 Try These Example Messages
Once you have the app open, you can test it with these examples to see how it handles context:

Spam Test: “Congratulations! You won $5000! Click this link right now to claim your cash reward!!”

Ham Test: “Hey, are we still meeting up tomorrow at 10am to review the project notes?”

 A Note on the Dataset
Because the training dataset (emails.csv) is incredibly large, I have excluded it from this repository and added it to the .gitignore to keep the repo lightweight. If you plan on re-running train_model.py yourself, you will need to grab the source dataset separately and place it in the root folder.

 What's Next? (Future Improvements)
This was an amazing learning experience, but there is always room to grow. In the future, I would love to:

Upgrade to Deep Learning models or try Transformers like BERT.

Implement specific filters for phishing email detection, not just standard spam.

Add support for Nepali language spam detection 🇳🇵

Clean up the UI/UX with better analytics dashboards.

About Me
I'm Birendra Joshi, an aspiring developer from Nepal 🇳🇵.

I built this project purely for learning and educational purposes to grow my skills in Machine Learning and Data Science. If you find this project interesting or useful, I would highly appreciate it if you could drop a star on this repository! ⭐
