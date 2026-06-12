import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = [pd.read_csv(file) for file in files]

df = pd.concat(dfs, ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["sales"] = df["quantity"] * df["price"]

output_df = df[["sales", "date", "region"]]

output_df.to_csv("formatted_sales_data.csv", index=False)

print("File created successfully!")