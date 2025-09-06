# ⚖️ Legal Document Assistant

Ever get lost in a super long legal document? This app is here to help!

It's a handy tool built with Streamlit that uses some smart AI from Hugging Face to read and understand dense legal texts. It'll whip up a quick summary for you and even let you ask questions about the document in a simple chat. So, whether you're a lawyer, a law student, or just trying to make sense of some complicated paperwork, this app's got your back!

*(Don't forget to add a screenshot of your running app!)*

## ✨ What Can It Do?

* **Get the Gist, Fast**: Got a massive document? Just upload it, and the app will give you the short version. It uses a special AI model that's great with long texts, so you don't have to read every single word!

* **Chat with Your Docs**: Once you've got the summary, you can literally chat with the document! Just type your questions in the chat box, and another smart AI will find the answers right from the text.

* **Handles Different Files**: It doesn't matter if your file is a `.pdf`, `.docx`, or a plain `.txt` – just upload it, and the app will handle it.

* **Super Easy to Use**: I built this with Streamlit, so the interface is clean and simple. No tech genius required!

* **Fast & Efficient**: The app is pretty smart – it only loads the heavy AI models once. That means after the first time you run it, it's much faster and ready to go when you are!

## 🛠️ The Tech Behind It

* **Backend**: Python

* **Web Framework**: Streamlit

* **NLP / AI**:

  * Hugging Face `transformers` library

  * PyTorch

* **File Processing**:

  * `PyPDF2` for PDF extraction

  * `python-docx` for DOCX extraction

## 🚀 Get it Running!

Ready to give it a try? Here's how to get everything set up on your own computer.

### What You'll Need

* Python (version 3.8 or newer)

* `pip` (which usually comes with Python)

### 1. Clone This Repo

First, grab the code from GitHub.

git clone https://github.com/your-username/legal-document-assistant.git
cd legal-document-assistant

### 2. Set Up a Virtual Environment (A Good Idea!)

This keeps all the project's packages neatly in one place.

* **On macOS/Linux:**

python3 -m venv venv
source venv/bin/activate

* **On Windows:**
  
python -m venv venv
.\venv\Scripts\activate

### 3. Install Everything It Needs

Run this command to install all the libraries listed in the `requirements.txt` file.

pip install -r requirements.txt

*(Heads up! The first time you run the app, it's going to download the AI models, which are pretty big. Make sure you have a good internet connection!)*

### 4. Fire It Up!

Alright, you're all set! To launch the app, just run this one command:

streamlit run app.py

A new tab should pop open in your browser with the running application. You're ready to go!

## 🧐 How to Use It

1. **Launch the app** with the command above.

2. **Upload a document**. You can either drag and drop a file or click the "Browse files" button.

3. **Let it think for a moment**. The app will work its magic and show you a summary.

4. **Start asking questions**! Just scroll down to the chat box and type away.

## 🧠 The Brains of the Operation

Wondering what's powering all this? It's these two awesome pre-trained models from the Hugging Face Hub:

* **Summarization**: [allenai/led-base-16384](https://huggingface.co/allenai/led-base-16384) - A model that's a beast at handling really long documents, making it perfect for legal texts.

* **Question Answering**: [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) - A super smart model that's great at finding the exact answer to a question within a chunk of text.


