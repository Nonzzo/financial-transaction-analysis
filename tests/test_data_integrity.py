# Test for connection
import pytest
import psycopg2

def test_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="financial_db",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        conn.close()
        assert True
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")




def test_data_population():
    conn = psycopg2.connect(
        dbname="financial_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Check if customers are populated
    cursor.execute("SELECT COUNT(*) FROM customers;")
    assert cursor.fetchone()[0] > 0, "No customers inserted"

    # Check if accounts are populated
    cursor.execute("SELECT COUNT(*) FROM accounts;")
    assert cursor.fetchone()[0] > 0, "No accounts inserted"

    # Check if transactions are populated
    cursor.execute("SELECT COUNT(*) FROM transactions;")
    assert cursor.fetchone()[0] > 0, "No transactions inserted"

    conn.close()
