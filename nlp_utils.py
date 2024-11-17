from transformers import pipeline

# Load the NLP model (can be extended for more complex logic)
qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

def evaluate_answer(question, context, student_answer):
    # Run NLP model to evaluate answer
    response = qa_pipeline(question=question, context=context)

    # Compare the extracted answer with student's response
    model_answer = response['answer']
    if model_answer.lower() in student_answer.lower():
        score = 10  # Full marks
        rationale = "Answer matches the textbook context closely."
    else:
        score = 5  # Partial marks
        rationale = "Answer partially matches the textbook context."

    return score, rationale

