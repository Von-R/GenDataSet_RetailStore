import pandas as pd
import numpy as np
import random
from random import randint
from faker import Faker

# Set seed for reproducibility
np.random.seed(0)
fake = Faker()


# Generate a random date
def generate_date(n):
    start_date = pd.to_datetime('01-01-2020')
    end_date = pd.to_datetime('31-12-2022')
    return start_date + (end_date - start_date) * np.random.rand(n)


# Generate a random product price
def generate_price(n):
    return np.random.uniform(5, 200, n)


# Generate a random quantity
def generate_quantity(n):
    return np.random.randint(1, 5, n)


# Generate a random age
def generate_age(n):
    return np.random.randint(18, 70, n)


# Generate a random product category
def generate_product_category(n):
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Health']
    return np.random.choice(categories, n)


# Generate a random product name
def generate_product_name(n):
    product_names = ['Smartphone', 'Laptop', 'Headphones', 'T-shirt', 'Jeans', 'Dress', 'Shoes', 'Coffee Maker',
                     'Blender', 'Cookware Set', 'Book1', 'Book2', 'Book3', 'Lipstick', 'Skincare Set', 'Perfume']
    return np.random.choice(product_names, n)


# Generate a random location
def generate_location(n):
    return [fake.city() for _ in range(n)]


# Generate a random customer ID
def generate_customer_id(n):
    return [fake.unique.random_number(digits=5, fix_len=True) for _ in range(n)]


n = 1000  # Number of records

data = {
    'CustomerID': generate_customer_id(n),
    'PurchaseDate': generate_date(n),
    'ProductID': np.arange(1, n + 1),
    'ProductName': generate_product_name(n),
    'ProductCategory': generate_product_category(n),
    'ProductPrice': generate_price(n),
    'Quantity': generate_quantity(n),
    'TotalPrice': [0] * n,  # We'll calculate this later
    'CustomerAge': generate_age(n),
    'CustomerLocation': generate_location(n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate TotalPrice
df['TotalPrice'] = df['ProductPrice'] * df['Quantity']

# Introduce some missing values
df.loc[df.sample(frac=0.05).index, 'ProductPrice'] = np.nan
df.loc[df.sample(frac=0.03).index, 'CustomerAge'] = np.nan
df.loc[df.sample(frac=0.02).index, 'CustomerLocation'] = np.nan

# Introduce some outliers in ProductPrice
df.loc[df.sample(frac=0.01).index, 'ProductPrice'] = df['ProductPrice'] * 10

# Convert PurchaseDate to datetime format
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

df.head()
