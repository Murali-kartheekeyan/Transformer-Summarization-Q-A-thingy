# document_processor.py
import textwrap

def _split_text_into_chunks(text, max_chunk_length=1024):
    """
    Splits text into chunks of a specified maximum length without breaking words.
    A more advanced version would use the model's tokenizer to count tokens.
    """
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 < max_chunk_length:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def summarize_text(summarizer, text, max_len=256, min_len=50):
    """
    Generates a summary for the given text, handling long documents by chunking.
    """
    # The context window for the Pegasus model is 1024 tokens. 
    # We'll use a slightly smaller chunk size to be safe.
    # NOTE: This simple character-based chunking is an approximation. A more precise
    # method uses the model's tokenizer to count tokens, but this is a robust start.
    
    # Check if the text is short enough to not need chunking
    if len(text) < 1024:
        try:
            summary_list = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            return textwrap.fill(summary_list[0]['summary_text'], width=80)
        except Exception as e:
            return f"Could not generate summary. Error: {e}"

    # If the text is long, chunk it
    print("Document is long. Splitting into chunks for summarization...")
    chunks = _split_text_into_chunks(text, max_chunk_length=1000) # Use 1000 to be safe
    combined_summary = ""

    try:
        for i, chunk in enumerate(chunks):
            print(f"Summarizing chunk {i+1}/{len(chunks)}...")
            # We adjust min/max length for chunks to be proportional
            chunk_summary_list = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            combined_summary += chunk_summary_list[0]['summary_text'] + " "
        
        return textwrap.fill(combined_summary.strip(), width=80)
    except Exception as e:
        return f"An error occurred during chunked summarization: {e}"


def answer_question(question_answerer, question, context):
    """Answers a question based on the provided context using the Q&A pipeline."""
    # For Q&A, we still pass the full context, as the pipeline is designed
    # to find the single best span within the text. Some pipelines can handle
    # long documents internally, but if this errors, chunking would be needed here too.
    try:
        result = question_answerer(question=question, context=context)
        answer = result['answer']
        score = result['score']
        return f"{answer} (Confidence: {score:.4f})"
    except Exception as e:
        # Check for the specific sequence length error
        if "sequence length" in str(e):
             return "Could not find an answer. The document is too long for the Q&A model's context window."
        return f"Could not find an answer. Error: {e}"