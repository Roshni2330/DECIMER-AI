from modules.pdf_loader import PDFLoader

loader = PDFLoader()

pdf_info = loader.save_pdf(
    r"C:\Users\BIT\OneDrive\Desktop\DECIMERAI2.0\input_pdfs\decimer.ai.pdf"
)

print("\nPDF Information")
print("=" * 50)

for key, value in pdf_info.items():
    print(f"{key:15} : {value}")