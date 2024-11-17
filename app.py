from flask import Flask, request, jsonify, render_template
from ocr_utils import extract_text_from_pdf
from nlp_utils import evaluate_answer
from db_utils import create_db, insert_response

app = Flask(__name__)

# Initialize the database
create_db()

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['pdf']
    student_id = request.form['student_id']
    file_path = f'student_responses/{student_id}.pdf'
    file.save(file_path)

    # OCR Processing
    extracted_text = extract_text_from_pdf(file_path)

    # NLP Processing
    context = "This is the textbook content. It explains the process of photosynthesis..."  # Example context
    question = "What is photosynthesis?"
    score, rationale = evaluate_answer(question, context, extracted_text)

    # Save to Database
    insert_response(student_id, extracted_text, score)

    return jsonify({"student_id": student_id, "score": score, "rationale": rationale})

if __name__ == '__main__':
    app.run(debug=True)
