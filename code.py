import re
import os
from PyPDF2 import PdfReader

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def mask_pii(value, pii_type):
    if pii_type == "AADHAAR":
        return "XXXX XXXX XXXX"
    elif pii_type == "PAN":
        return "XXXXX" + value[5:]
    elif pii_type == "DL":
        return "XX" + value[2:]
    return value

def detect_pii(content):
    aadhaar_pattern = r"\b\d{4}\s?\d{4}\s?\d{4}\b"
    pan_pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
    dl_pattern = r"\b[A-Z]{2}[0-9]{2}[0-9A-Z]{11}\b"

    aadhaar = re.findall(aadhaar_pattern, content)
    pan = re.findall(pan_pattern, content)
    dl = re.findall(dl_pattern, content)

    print("\n--- Aadhaar Numbers ---")
    for number in aadhaar:
        print("Found:", number, "→ Masked:", mask_pii(number, "AADHAAR"))

    print("\n--- PAN Numbers ---")
    for number in pan:
        print("Found:", number, "→ Masked:", mask_pii(number, "PAN"))

    print("\n--- Driving License Numbers ---")
    for number in dl:
        print("Found:", number, "→ Masked:", mask_pii(number, "DL"))

def main():
    file_path = input("Enter path to .txt or .pdf file: ")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if file_path.endswith(".txt"):
        content = read_txt(file_path)
    elif file_path.endswith(".pdf"):
        content = read_pdf(file_path)
    else:
        print("Only .txt and .pdf files are supported.")
        return

    detect_pii(content)

if __name__ == "__main__":
    main()