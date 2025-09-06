from model_loader import load_models
from document_processor import summarize_text, answer_question
from file_handler import extract_text_from_file 

def run_cli_app():
    summarizer, question_answerer = load_models()
    if not summarizer or not question_answerer:
        return

    print("\n--- Legal Document Assistant ---")
    
    file_path = input("Please enter the full path to your document (.txt, .docx, or .pdf):\n").strip()
    document_text, error = extract_text_from_file(file_path)

    if error:
        print(f"\nError: {error}")
        return
    
    if not document_text or not document_text.strip():
        print("\nWarning: The extracted document is empty. This can happen with scanned PDFs or empty files.")
        return
        
    print("\nFile read successfully!")
    print("\nGenerating summary...")
    summary = summarize_text(summarizer, document_text)
    print("\n--- Document Summary ---")
    print(summary)
    
    print("\n--- Ask Questions About the Document ---")
    print("Type your question and press Enter. Type 'exit' to quit.")

    while True:
        question = input("\nQuestion: ")
        if question.lower() == 'exit':
            print("Exiting the Q&A session. Goodbye!")
            break
        
        if not question:
            print("Please enter a question.")
            continue
            
        answer = answer_question(question_answerer, question, document_text)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    run_cli_app()