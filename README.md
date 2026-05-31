
📧 Spam Email Classifier
     <img width="1919" height="981" alt="image" src="https://github.com/user-attachments/assets/da5c072e-78b3-4df5-a4cb-d058c098ee79" />


An email classifier for your terminal and web browser. Build with python 
with streamlit library for those beautiful UI and scikit-learn for 
detecting the actual spam.

NOTE: For running this project, you will need to install the 
requirements first, so you can clone repo then run

pip install -r requirements.txt

Then

python app.py

Custom Features
Custom data cleaning: I used a massive dataset of 192,000 emails then 
used TF-IDF vectorizer script to convert it into clean numerical data.

Beautiful UI: I think the Streamlit interface looks beautiful (I'm 
not a good designer thooo), feel free for suggestions.

High Accuracy: I added a machine learning backend using Multinomial Naive 
Bayes that scores a massive 96.38% overall accuracy on test data.

<img width="937" height="266" alt="image" src="https://github.com/user-attachments/assets/c047a873-045a-4329-8745-f15677376f42" />



For source code building
Make sure you install the requrements first
pip install -r requirements.txt

Then u can run:
python train_model.py

AI declaration:
Logical Errors: Sometimes when I was stuck at some logical errors (like 
handling Streamlit Cloud ModuleNotFoundErrors), I used gemini to guide 
me.. but I tried to understand the fix too.

Repetitive work: I did most of the work but sometimes when the work was 
just tooo basic and repetitive like: breaking down what precision and 
recall mean for the model metrics output, I again used gemini.

🌐 Live Demo Link
You can test the live web app out right here:
👉 https://email-classifier11.streamlit.app/

🇳🇵 About Me
I'm Birendra Joshi, an aspiring developer from Nepal. 
NOTE: THIS PROJECT IS FOR MY MACHINE LEARNING, LEARNING PURPOSES. I AM 
TRYING TO LEAN AND GROW. If you like this project, consider giving it 
a star on GitHub ⭐
======================================================================
