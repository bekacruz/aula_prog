import sys
import pandas as pd
table = sys.argv[1]
coeficient_m = float(sys.argv[2])
coeficient_b = float(sys.argv[3])
df = pd.read_excel(table)
df_q = df[['Target_Name', 'Stage']].drop_duplicates()
df_q['Quantity'] = 10**((df['CT']-coeficient_b)/coeficient_m)
df_f = pd.merge(df,df_q)
df_f.to_excel("C:/Users/BECKY/Documents/Quant_Abs.xlsx", sheet_name="CT_Absoluto")
print(df_f)