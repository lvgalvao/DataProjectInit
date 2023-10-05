import os
import glob
import pandas as pd

# Configurações de diretórios e nomes de arquivos
input_folder = "data/input"  # Altere para o caminho da sua pasta de entrada
output_folder = "data/output"    # Altere para o caminho da sua pasta de saída
output_file_name = "consolidado.xlsx"

# Extract
files = glob.glob(os.path.join(input_folder, "*.xlsx"))
if not files:
    raise ValueError("No Excel files found in the specified folder")
all_data = [pd.read_excel(file) for file in files]

if not all_data:
    raise ValueError("No data to transform")

# Transform
consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)

# Load
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
consolidated_df.to_excel(os.path.join(output_folder, output_file_name), index=False)

print("Processamento concluído!")
