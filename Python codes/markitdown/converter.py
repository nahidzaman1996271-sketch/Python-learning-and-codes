from markitdown import MarkItDown

md = MarkItDown()

# Convert PPTX
result_pptx = md.convert(r"C:\Users\AMCS\Downloads\Cap.docx")
print(result_pptx.markdown)

# Save PPTX result
with open("output_pptx.md", "w", encoding="utf-8") as f:
    f.write(result_pptx.markdown)

# Convert Word document
result_docx = md.convert(r"D:\your-folder\document.docx")
print(result_docx.markdown)

# Save DOCX result
with open("output_docx.md", "w", encoding="utf-8") as f:
    f.write(result_docx.markdown)