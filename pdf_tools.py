from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber

# Merge PDFs
def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

    print(f"Merged PDF saved to: {output_path}")


# Extract Text
def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


# Add Watermark
def add_watermark(input_pdf, watermark_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    watermark_reader = PdfReader(watermark_pdf)

    watermark_page = watermark_reader.pages[0]

    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"Watermarked PDF saved to: {output_pdf}")