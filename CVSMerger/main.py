import pandas as pd
import os
from glob import glob

# Folder containing the CSV files
csvs_folder = "csvs"

# List all CSV files in the folder
arquivos = glob(os.path.join(csvs_folder, "*.csv"))

dfs = []
for arquivo in arquivos:
    print(f"Lendo: {arquivo}")
    df = pd.read_csv(arquivo)

    # Remove duplicated columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Remove columns where all values are NaN
    df = df.dropna(axis=1, how='all')

    # Remove lines where the first column is NaN
    primeira_coluna = df.columns[0]
    df = df[df[primeira_coluna].notna()]

    dfs.append(df)

# Concatenate all DataFrames into one
df_final = pd.concat(dfs, ignore_index=True)

# Save the final DataFrame to a new CSV file
output_path = "csv_unified.csv"
df_final.to_csv(output_path, index=False)
print(f"\n✅ File saved as: {output_path}")
