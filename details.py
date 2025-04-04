def create_sample_file():
    sample_text = """This is a test document for detecting PII.

My Aadhaar number is 1234 5678 9101.
My PAN is ABCDE1234F.
My Driving License number is MH12AB1234567890.

Please ensure this information is masked or removed if not necessary.
"""
    file_name = "sample.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(sample_text)

    print(f"Sample file '{file_name}' created successfully.")

if _name_ == "_main_":
    create_sample_file()