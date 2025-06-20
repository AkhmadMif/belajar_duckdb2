import duckdb
import pandas as pd
import polars as pl

# Step 1: Baca 1 file CSV dengan Pandas
df_pandas = pd.read_excel("D:/Learning/dataset/belajar_duckdb2/final dataset.xlsx")

# Konversi DataFrame pandas ke Polars
df_polars = pl.from_pandas(df_pandas)

# Step 2: Query SQL dengan DuckDB ke Pandas DataFrame
# Jika kamu ingin menggunakan DuckDB untuk SQL, pastikan terlebih dahulu file CSV sudah dibaca di DuckDB
# Karena kita bekerja dengan Polars, lebih baik menggunakan Polars untuk query, 
# atau menggunakan Pandas terlebih dahulu ke DuckDB.

# Query DuckDB untuk data yang ada di pandas
result = duckdb.query("""
    SELECT Q1, Q2, Q3, Q4, Q5, Q6 
    FROM df_pandas
""").df()

# Step 3: Proses dengan Polars (menggunakan Polars untuk sorting dan transformasi lebih lanjut)
df_polars_result = pl.from_pandas(result)
final = df_polars_result.sort("Q1")

# Step 4: Tampilkan hasil
print(final)