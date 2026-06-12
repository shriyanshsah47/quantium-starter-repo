import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Read and combine all files
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Keep only pink morsels
df = df[df["product"] == "pink morsel"]

# Convert price from "$3.00" to 3.00
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
output_df = df[["sales", "date", "region"]]

# Save output
output_df.to_csv("formatted_sales_data.csv", index=False)

print("formatted_sales_data.csv created successfully!")