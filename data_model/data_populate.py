# -------------------------------
# Step 2: Python Script for Data Population
# -------------------------------

import psycopg2
from faker import Faker
import random

# Database connection setup
def connect_db():
    return psycopg2.connect(
        dbname="gisdb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def populate_data():
    faker = Faker()
    conn = connect_db()
    cursor = conn.cursor()

    # Insert customers
    for _ in range(100):
        cursor.execute(
            """
            INSERT INTO customers (name, dob, email, phone, address, kyc_status, risk_profile)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """,
            (
                faker.name(),
                faker.date_of_birth(minimum_age=18, maximum_age=90),
                faker.email(),
                faker.phone_number(),
                faker.address(),
                random.choice([True, False]),
                random.choice(["low", "medium", "high"])
            )
        )

    conn.commit()

    # Insert accounts
    cursor.execute("SELECT id FROM customers;")
    customer_ids = [row[0] for row in cursor.fetchall()]

    for customer_id in customer_ids:
        for _ in range(random.randint(1, 3)):
            cursor.execute(
                """
                INSERT INTO accounts (customer_id, account_type, balance, status)
                VALUES (%s, %s, %s, %s);
                """,
                (
                    customer_id,
                    random.choice(["checking", "savings", "credit"]),
                    round(random.uniform(100, 10000), 2),
                    "active"
                )
            )

    conn.commit()
    
     # Insert transactions
    cursor.execute("SELECT id FROM accounts;")
    account_ids = [row[0] for row in cursor.fetchall()]

    for account_id in account_ids:
        for _ in range(random.randint(5, 20)):
            cursor.execute(
                """
                INSERT INTO transactions (account_id, amount, type, latitude, longitude, country_code)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                (
                    account_id,
                    round(random.uniform(1, 5000), 2),
                    random.choice(["credit", "debit"]),
                    round(random.uniform(-90, 90), 6),
                    round(random.uniform(-180, 180), 6),
                    faker.country_code()
                )
            )

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    populate_data()