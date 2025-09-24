import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()
random.seed(42)
Faker.seed(42)

categories = ["Furniture", "Office Supplies", "Technology"]
sub_categories = {
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art", "Envelopes"],
    "Technology": ["Phones", "Accessories", "Machines", "Copiers"]
}
regions = ["East", "West", "Central", "South"]
segments = ["Consumer", "Corporate", "Home Office"]
states = ["California", "Texas", "New York", "Florida", "Illinois", "Pennsylvania", "Ohio", "Georgia", "Michigan", "North Carolina"]

n = 500
data = []
for i in range(1, n+1):
    category = random.choice(categories)
    sub_category = random.choice(sub_categories[category])
    region = random.choice(regions)
    state = random.choice(states)
    segment = random.choice(segments)
    order_date = fake.date_between(start_date="-3y", end_date="today")
    sales = round(random.uniform(20, 2000), 2)
    quantity = random.randint(1, 10)
    discount = round(random.choice([0, 0.1, 0.2, 0.3]), 2)
    profit = round(sales * random.uniform(-0.2, 0.3), 2)
    order_id = f"ORD-{1000+i}"
    product_name = fake.word().capitalize() + " " + sub_category
    
    data.append([order_id, order_date, region, state, category, sub_category, product_name, sales, quantity, discount, profit, segment])

df = pd.DataFrame(data, columns=[
    "Order ID", "Order Date", "Region", "State", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit", "Segment"
])

# Add derived fields
df["Year"] = pd.to_datetime(df["Order Date"]).dt.year
df["MonthYear"] = pd.to_datetime(df["Order Date"]).dt.to_period("M").astype(str)
df["Profit Margin"] = df["Profit"] / df["Sales"].replace({0: pd.NA})

# Save datasets
df.to_csv("superstore_clean.csv", index=False)
