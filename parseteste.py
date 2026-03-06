from llama_parse import LlamaParse
import os
from pathlib import Path


parser = LlamaParse(
   api_key="llx-5Fq2oMo4Q43L6W69bCq5EEMxn57FT573OHfnVjhNF527N6us",
   result_type="markdown",
   extract_charts=True,
   auto_mode=True,
   auto_mode_trigger_on_image_in_page=True,
   auto_mode_trigger_on_table_in_page=True,
)

docs_folder = "docs"
outputs_folder = "outputs"

# Create outputs folder if it doesn't exist
Path(outputs_folder).mkdir(exist_ok=True)

# Get list of PDFs in docs folder
pdf_files = [f for f in os.listdir(docs_folder) if f.endswith('.pdf')]

print(f"Encontrados {len(pdf_files)} PDFs em {docs_folder}/")
print("-" * 50)

# Get list of already processed files
processed_files = set(os.listdir(outputs_folder)) if os.path.exists(outputs_folder) else set()

for pdf_file in pdf_files:
    # Generate output filename (replace .pdf with .md)
    output_file = pdf_file.replace('.pdf', '.md')

    # Check if already processed
    if output_file in processed_files:
        print(f"✓ {pdf_file} → já foi processado (skip)")
        continue

    print(f"→ Processando: {pdf_file}...")

    file_path = os.path.join(docs_folder, pdf_file)
    output_path = os.path.join(outputs_folder, output_file)

    try:
        with open(file_path, "rb") as f:
            extra_info = {"file_name": file_path}
            documents = parser.load_data(f, extra_info=extra_info)

        # Write to markdown file
        with open(output_path, "w", encoding="utf-8") as f:
            for doc in documents:
                f.write(doc.text)

        print(f"✓ {pdf_file} → salvo como {output_file}")

    except Exception as e:
        print(f"✗ Erro ao processar {pdf_file}: {str(e)}")

print("-" * 50)
print("Processamento concluído!")
