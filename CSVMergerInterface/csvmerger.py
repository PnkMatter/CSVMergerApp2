import streamlit as st
import pandas as pd
from io import BytesIO

st.title("CSV merger 2.0")

# Allow users to upload multiple CSV files
uploaded_files = st.file_uploader("Selecione os arquivos CSV", type="csv", accept_multiple_files=True)

if uploaded_files:
    dfs = []
    for file in uploaded_files:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file)
        
        # Remove duplicated columns
        df = df.loc[:, ~df.columns.duplicated()]
        
        # Remove empty columns
        df = df.dropna(axis=1, how='all')
        
        # Remove rows where the first column is NaN
        first_col = df.columns[0]
        df = df[df[first_col].notna()]
        
        dfs.append(df)

    # Concatenate all DataFrames into one
    df_final = pd.concat(dfs, ignore_index=True)

    st.write("Prévia do CSV unificado:")
    st.dataframe(df_final)

    # Download for the unified CSV
    def convert_df(df):
        output = BytesIO()
        df.to_csv(output, index=False)
        return output.getvalue()

    csv_data = convert_df(df_final)

    st.download_button(
        label="📥 Baixar CSV Unificado",
        data=csv_data,
        file_name="csv_unificado.csv",
        mime="text/csv"
    )

# Made by Gabriel Resende [PnkMatter -> Github]
st.markdown("Made by Gabriel Resende")