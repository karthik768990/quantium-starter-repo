import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# List of CSV files
csv_files = list(data_path.glob("*.csv"))

processed_frames = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Select required columns
    df = df[["Sales", "date", "region"]]

    # Rename for consistency
    df = df.rename(columns={
        "date": "Date",
        "region": "Region"
    })

    processed_frames.append(df)

# Combine all files into one DataFrame
final_df = pd.concat(processed_frames, ignore_index=True)

# Save output
final_df.to_csv("pink_morsels_sales.csv", index=False)

print("✅ Data processing complete. Output saved as pink_morsels_sales.csv")
