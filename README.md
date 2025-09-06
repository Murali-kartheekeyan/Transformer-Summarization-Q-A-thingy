⚖️ Legal Document Assistant
An interactive web application built with Streamlit that uses Hugging Face Transformer models to summarize legal documents and answer questions about their content.

This tool is designed to help legal professionals, students, and anyone working with dense legal texts to quickly grasp the key points of a document and find specific information through a conversational interface.

(Add a screenshot of your running application here)

✨ Features
Automatic Summarization: Upload a document, and the app generates a concise summary using the allenai/led-base-16384 model, which is specifically designed for long-form text.

Interactive Q&A: After summarizing, a chat interface allows you to ask specific questions about the document's content. The deepset/roberta-base-squad2 model finds the answers directly from the text.

Multiple File Formats: Supports uploading documents in various common formats:

.pdf

.docx

.txt

User-Friendly Interface: A clean and intuitive UI built with Streamlit, making it easy for anyone to use without a technical background.

Efficient Model Caching: Streamlit's caching ensures that the large NLP models are loaded into memory only once, providing a fast and smooth user experience on subsequent uses.

🛠️ Tech Stack
Backend: Python

Web Framework: Streamlit

NLP / AI:

Hugging Face transformers library

PyTorch

File Processing:

PyPDF2 for PDF extraction

python-docx for DOCX extraction

🚀 Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python 3.8 or higher

pip (Python package installer)

1. Clone the Repository
git clone [https://github.com/your-username/legal-document-assistant.git](https://github.com/your-username/legal-document-assistant.git)
cd legal-document-assistant

2. Create a Virtual Environment (Recommended)
It's good practice to create a virtual environment to manage project dependencies.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
The project comes with a requirements.txt file that lists all the necessary libraries.

pip install -r requirements.txt

(Note: The first time you run the app, the transformer models (several GBs in size) will be downloaded and cached on your machine. This requires a stable internet connection.)

4. Run the Streamlit App
Once the dependencies are installed, you can start the application with a single command:

streamlit run app.py

Your default web browser will open a new tab at http://localhost:8501 with the running application.

usage How to Use
Launch the application using the command above.

Upload a document by clicking the "Browse files" button or by dragging and dropping a file into the uploader.

Wait for the analysis: The application will automatically process the document and display a summary.

Ask questions: Scroll down to the chat interface and type your questions about the document to receive instant answers.

🧠 Models Used
This project leverages state-of-the-art pre-trained models from the Hugging Face Hub:

Summarization: allenai/led-base-16384 - A Longformer Encoder-Decoder model capable of handling long sequences (up to 16,384 tokens), making it ideal for lengthy legal documents.

Question Answering: deepset/roberta-base-squad2 - A robust RoBERTa-based model fine-tuned on the SQuAD 2.0 dataset for extractive question answering.

💡 Future Improvements
OCR for Scanned Documents: Integrate an OCR (Optical Character Recognition) library like Tesseract to extract text from scanned PDFs.

Batch Processing: Allow users to upload and analyze multiple documents at once.

Advanced Legal Models: Experiment with models specifically fine-tuned on larger legal corpora for potentially higher accuracy.

Deployment: Containerize the application with Docker and deploy it to a cloud service like Streamlit Community Cloud or Hugging Face Spaces.