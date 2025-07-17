📊 ***CSV Cleaner & Merger***

This project allows you to merge multiple .csv files with the same structure while cleaning the data by:

    Removing duplicated columns

    Dropping empty columns

    Removing rows where the first column is empty

It supports two modes:

    ✅ Web Interface using Streamlit

    ✅ Command-line script (no interface)

⚙️ Requirements

Install the required packages with:

    pip install pandas streamlit

🖥️ Mode 1 — Web Interface (Streamlit)
🔄 How to Use

  Run the app with:

    streamlit run app_streamlit.py

  Upload one or more .csv files with the same structure.

  The app will:

      Remove duplicate columns

      Drop columns that are completely empty

      Remove rows where the first column is empty

  You’ll be able to preview the final result and download the cleaned merged file.

🧪 Example:
```
┌──────────┬──────────┬──────────┬──────────┐
│ Column 1 │ Column 2 │ Column 3 │  ...     │
├──────────┼──────────┼──────────┼──────────┤
│ 1        │ a        │ a        │          │
│ 2        │ b        │ b        │          │
│ null     │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```
🧾 Mode 2 — Terminal Script (No Interface)
📁 Expected Structure

Create a folder called csvs in the same directory as the script and place all your .csv files there.
▶️ How to Run

python app_terminal.py

🔍 What It Does

  Reads all .csv files in the csvs folder

  Cleans each file by:

    Removing duplicated columns

    Dropping columns that are fully empty

    Removing rows where the first column is empty

  Merges all files into one csv_unificado.csv

📂 Project Structure

  ```📁 your-repo/
  ├── 📁 csvs/                # Place your input CSVs here (for terminal mode)
  ├── app_streamlit.py       # Streamlit version (web UI)
  ├── app_terminal.py        # Terminal version (no UI)
  └── README.md              # This file
```
🧠 Notes

    All .csv files should have the same column structure.

    The script will keep only the first occurrence of each column name.

    Rows where the first column is empty will be discarded.

👨‍💻 Author

Developed by **PnkMatter**

Feel free to connect with me on LinkedIn or check out my projects on GitHub

📃 License

**This project is licensed under the MIT License.**
