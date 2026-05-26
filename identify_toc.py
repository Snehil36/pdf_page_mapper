from google import genai
import pymupdf
import os

client = genai.Client(api_key=os.getenv("PDF_OFFSETTER"))

def find_toc(pdf_path):

    doc = pymupdf.open(pdf_path)

    # Incase pdf is over the max page size of 100 just takes first 50
    condensed_doc = pymupdf.open()
    condensed_doc.insert_pdf(doc, from_page = 0, to_page = 49)
    condensed_doc.save("temp_first50.pdf")

    file = client.files.upload(file="temp_first50.pdf")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            file,
            """Find the table of contents in this PDF.
            1. List all chapter titles and their printed page numbers
            2. Tell me what PDF page number the first chapter actually starts on
            Reply in this format:
            FIRST_CHAPTER_PRINTED_PAGE: <number>
            FIRST_CHAPTER_PDF_PAGE: <number>
            TOC:
            <chapter title> <@> <printed page number>
            """
        ]
    )
    os.remove("temp_first50.pdf")
    return response.text

