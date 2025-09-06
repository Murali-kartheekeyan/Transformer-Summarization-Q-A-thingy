import streamlit as st
from transformers import pipeline
import docx
import PyPDF2
import textwrap

st.set_page_config(
    page_title="Legal Document Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_models():
    """Loads and returns the summarization and question-answering pipelines."""
    try:
        summarizer = pipeline("summarization", model="allenai/led-base-16384")
        question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")
        return summarizer, question_answerer
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.error("Please ensure you have a stable internet connection and required libraries are installed.")
        return None, None

def extract_text_from_uploaded_file(uploaded_file):
    
    if uploaded_file.name.endswith('.txt'):
        return uploaded_file.getvalue().decode('utf-8')
    elif uploaded_file.name.endswith('.docx'):
        try:
            doc = docx.Document(uploaded_file)
            return '\n'.join([para.text for para in doc.paragraphs])
        except Exception as e:
            st.error(f"Error reading .docx file: {e}")
            return ""
    elif uploaded_file.name.endswith('.pdf'):
        text = ""
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
        except Exception as e:
            st.error(f"Error reading .pdf file: {e}")
            return ""
    return ""

def summarize_text(summarizer, text):
    """Generates a summary for the given text."""
    if not text:
        return "No text to summarize."
    try:
        summary_list = summarizer(text, max_length=512, min_length=50, do_sample=False)
        return textwrap.fill(summary_list[0]['summary_text'], width=80)
    except Exception as e:
        return f"Could not generate summary. Error: {e}"

def answer_question(question_answerer, question, context):
    """Answers a question based on the provided context."""
    if not context:
        return "Please provide a document context first."
    try:
        result = question_answerer(question=question, context=context)
        return f"{result['answer']} (Confidence: {result['score']:.2%})"
    except Exception:
        return "Could not find an answer in the document."

def main():
    st.title("⚖️ Legal Document Assistant")
    st.sidebar.header("Instructions")
    st.sidebar.info(
        "1. **Upload a document** (.txt, .docx, or .pdf).\n"
        "2. The app will automatically generate a summary.\n"
        "3. **Ask questions** about the document in the chat box below."
    )

    with st.spinner("Loading NLP models... This may take a few minutes on first run."):
        summarizer, question_answerer = load_models()

    if not summarizer or not question_answerer:
        st.stop()

    uploaded_file = st.file_uploader(
        "Upload your legal document",
        type=['txt', 'docx', 'pdf'],
        help="Supports .txt, .docx, and .pdf files."
    )

    if 'document_text' not in st.session_state:
        st.session_state.document_text = ""
    if 'summary' not in st.session_state:
        st.session_state.summary = ""
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if uploaded_file is not None:
        with st.spinner("Analyzing document..."):
            extracted_text = extract_text_from_uploaded_file(uploaded_file)
            st.session_state.document_text = extracted_text
            
            summary = summarize_text(summarizer, extracted_text)
            st.session_state.summary = summary
            
            st.session_state.messages = [] 
    
    if st.session_state.summary:
        st.subheader("📄 Document Summary")
        st.info(st.session_state.summary)

        with st.expander("View Full Document Text"):
            st.text_area("Document Content", st.session_state.document_text, height=300)

    if st.session_state.document_text:
        st.subheader("💬 Ask Questions About The Document")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What is your question?"):
            
            with st.chat_message("user"):
                st.markdown(prompt)
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            
            with st.spinner("Searching for an answer..."):
                answer = answer_question(question_answerer, prompt, st.session_state.document_text)
                response = f"**Answer:** {answer}"

            
            with st.chat_message("assistant"):
                st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
