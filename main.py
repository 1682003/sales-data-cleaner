import csv
import json

USD_TO_INR = 83

clean_records = []
seen_products = set()  # to store (product_name, price_usd)

# Read the CSV file
with open("sales.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        product_id = int(row[0])

        # Clean product name
        product_name = row[1].replace('"', '').strip()

        # Clean and convert price
        price_cleaned = row[2].replace('$', '').strip()
        price_usd = float(price_cleaned)

        # Convert USD to INR
        price_inr = price_usd * USD_TO_INR

        country = row[3].strip()

        # Deduplication based on Product Name + Price
        key = (product_name, price_usd)
        if key not in seen_products:
            seen_products.add(key)
            clean_records.append({
                "product_id": product_id,
                "product_name": product_name,
                "price_inr": price_inr,
                "country": country
            })

# Write clean data to JSON
with open("clean_sales.json", "w") as json_file:
    json.dump(clean_records, json_file, indent=4)

print("clean_sales.json file created successfully.")
