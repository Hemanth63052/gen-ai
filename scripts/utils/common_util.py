from pypdf import PdfReader

class CommonHandler:

    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        text = ""
        if pdf_path is not None:
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    @staticmethod
    def split_text(text, chunk_size=500, overlap=100):
        chunks = []
        start = 0
        while start < len(text):
            end = min(len(text), start + chunk_size)
            chunks.append(text[start:end])
            start += chunk_size - overlap  # Allow overlap for context between chunks
        return chunks