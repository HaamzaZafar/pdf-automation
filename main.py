from pdf_tools import merge_pdfs, extract_text, add_watermark

try:
    # Merge PDFs
    pdfs = [
        "input/file1.pdf",
        "input/file2.pdf"
    ]

    merge_pdfs(pdfs, "output/merged.pdf")

    # Extract Text
    text = extract_text("input/file1.pdf")

    print("\nExtracted Text:\n")
    print(text)

    # Add Watermark
    add_watermark(
        "input/file1.pdf",
        "input/watermark.pdf",
        "output/watermarked.pdf"
    )

    print("\nProject executed successfully")

except Exception as e:
    print(f"Error: {e}")