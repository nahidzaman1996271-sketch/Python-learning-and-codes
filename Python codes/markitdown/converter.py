from markitdown import MarkItDown

md = MarkItDown()

# Convert Scripts
result = md.convert(r"G:\Fourth Semester\Software Development Capstone Project\Capstone Project\Scripts.docx")
print(result.markdown)

# Save the result
with open("output_scripts.md", "w", encoding="utf-8") as f:
    f.write(result.markdown)