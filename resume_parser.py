"""
Resume Parser Module
====================
Handles extraction of text content from PDF resume files.
"""

import os
import PyPDF2


def extract_text_from_pdf(filepath):
    """
    Extract text from a PDF file.

    Args:
        filepath (str): Path to the PDF file.

    Returns:
        str: Combined text from all pages of the PDF.
    """
    text = ""
    try:
        with open(filepath, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"[ERROR] Could not read '{filepath}': {e}")
    return text.strip()


def load_all_resumes(folder_path):
    """
    Load and extract text from all PDF resumes in a folder.

    Args:
        folder_path (str): Path to the folder containing PDF resumes.

    Returns:
        dict: A dictionary mapping {filename: extracted_text}.
    """
    resumes = {}

    if not os.path.isdir(folder_path):
        print(f"[ERROR] Resume folder not found: '{folder_path}'")
        return resumes

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"[WARNING] No PDF files found in '{folder_path}'")
        return resumes

    for filename in sorted(pdf_files):
        filepath = os.path.join(folder_path, filename)
        print(f"  Parsing: {filename} ... ", end="")
        text = extract_text_from_pdf(filepath)
        if text:
            resumes[filename] = text
            print("OK")
        else:
            print("SKIPPED (no text extracted)")

    return resumes
