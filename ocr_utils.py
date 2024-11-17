from pdf2image import convert_from_path
import pytesseract
import os

def extract_text_from_pdf(pdf_path):
    # Ensure the Tesseract OCR executable is installed and configured
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Convert PDF to images
    images = convert_from_path(pdf_path, 500)

    # Extract text from images
    extracted_text = ''
    for image in images:
        extracted_text += pytesseract.image_to_string(image)

    return extracted_text
