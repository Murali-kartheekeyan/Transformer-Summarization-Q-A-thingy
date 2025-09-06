import os
import docx
import PyPDF2

def _read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def _read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = [para.text for para in doc.paragraphs]
        return '\n'.join(full_text)
    except Exception as e:
        raise Exception(f"Error reading .docx file: {e}")


def _read_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error reading .pdf file: {e}")


def extract_text_from_file(file_path):
    """
    Identifies the file type and extracts text accordingly.
    Supports .txt, .docx, and .pdf files.
    Returns a tuple (text, error_message).
    """
    if not os.path.exists(file_path):
        return None, "Error: File not found at the specified path."

    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    try:
        if file_extension == '.txt':
            return _read_txt(file_path), None
        elif file_extension == '.docx':
            return _read_docx(file_path), None
        elif file_extension == '.pdf':
            return _read_pdf(file_path), None
        else:
            return None, f"Error: Unsupported file type '{file_extension}'. Please use .txt, .docx, or .pdf."
    except Exception as e:
        return None, f"An error occurred while processing the file: {e}"