import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Atualizador de Banco de Dados de Importação")

# Upload de arquivos
arquivo_antigo = st.file_uploader("📂 Upload do arquivo ANTIGO", type="csv")
arquivo_novo = st.file_uploader("📂 Upload do arquivo NOVO", type="csv")

# Exemplo de mapeamento (Argentina)
# 🔧 Basta alterar os pares conforme o país
mapeamento_colunas = {
    "ColunaNovo1": "ColunaAntigo1",
    "ColunaNovo2": "ColunaAntigo2",
    # ...
}

st.write("📑 Mapeamento de colunas configurado:")
st.json(mapeamento_colunas)

if arquivo_antigo and arquivo_novo:
    # Leitura dos CSVs
    df_antigo = pd.read_csv(arquivo_antigo)
    df_novo = pd.read_csv(arquivo_novo)

    # Seleciona e renomeia colunas do arquivo novo
    df_novo_filtrado = df_novo[list(mapeamento_colunas.keys())].rename(columns=mapeamento_colunas)

    # Concatena os DataFrames
    df_final = pd.concat([df_antigo, df_novo_filtrado], ignore_index=True)

    st.write("✅ Prévia do CSV atualizado:")
    st.dataframe(df_final)

    # Função para exportar CSV
    def convert_df(df):
        output = BytesIO()
        df.to_csv(output, index=False)
        return output.getvalue()

    csv_data = convert_df(df_final)

    st.download_button(
        label="📥 Baixar CSV Atualizado",
        data=csv_data,
        file_name="csv_atualizado.csv",
        mime="text/csv"
    )

st.markdown("Made by Gabriel Resende")
