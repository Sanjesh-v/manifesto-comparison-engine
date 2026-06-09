from pypdf import PdfReader

def extract_text(pdf_path):

    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text

    except Exception as e:
        return str(e)