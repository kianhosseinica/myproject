import csv
import os
from items.models import Item

def clean_price(price_str):
    # Remove any currency symbols and commas
    cleaned_price = price_str.replace('$', '').replace(',', '').strip()
    try:
        return float(cleaned_price)
    except ValueError:
        print(f"Could not convert price: {price_str}")
        return None

def load_items_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price_str = row['price']
                price = clean_price(price_str)
                if price is not None:
                    Item.objects.create(name=name, price=price)
        print("Items successfully loaded from CSV.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage:
file_path = '/Users/kianhosseini/Desktop/instagram/myproject/items 7.09.15 AM.csv'
load_items_from_csv(file_path)
