import sqlite3
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

def get_fake_product_data(start_date, end_date, product_categories):
    fake = Faker()
    synthetic_data = []

    date_range = (end_date - start_date).days
    date_generator = (start_date + timedelta(n) for n in range(date_range))
    for single_date in date_generator:
        for category in product_categories:
            date_str = single_date.strftime('%Y-%m-%d')
            price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
            synthetic_data.append((category, date_str, price))

    synthetic_df = pd.DataFrame(synthetic_data, columns=['product', 'date', 'price'])
    return synthetic_df

def prepare_db(db_name='consumption.db', 
    # Define product categories
    num_entries_per_product = 100, 
    product_categories = ['milk', 'dairy', 'fruits', 'eggs'],
    start_date = datetime(2022, 1, 1),
    end_date = datetime(2022, 3, 31),
):
    """
    Fill the database with generic historical consumption data on a set of grocery products.
    This data can then be used to train a model to predict the consumption of different products based on historical data.
    The model can then be used to predict the consumption of products in real-time.
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Create a table to store historical consumption data
    c.execute('''CREATE TABLE IF NOT EXISTS consumption
                 (product TEXT, date TEXT, consumption REAL)''')

    # Generate synthetic data
    synthetic_df = get_fake_product_data(start_date, end_date, product_categories)
    synthetic_df.to_sql('consumption', conn, if_exists='append', index=False, method='multi')

    return c

def get_historical_consumption(product, db_name='consumption.db'):
    # Connect to the database
    c = prepare_db()

    c.execute("SELECT * FROM consumption WHERE product=?", (product,))
    data = c.fetchall()
    return data
