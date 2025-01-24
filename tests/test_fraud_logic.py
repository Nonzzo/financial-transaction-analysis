import pytest
import psycopg2

# est Fraud Detection Logic

def test_velocity_checks():
    conn = psycopg2.connect(
        dbname="financial_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Run velocity check query
    cursor.execute("""
        SELECT account_id, COUNT(*) AS transaction_count
        FROM transactions
        WHERE timestamp > NOW() - INTERVAL '1 HOUR'
        GROUP BY account_id
        HAVING COUNT(*) > 5;
    """)
    results = cursor.fetchall()
    assert len(results) > 0, "No velocity anomalies detected"

    conn.close()


# Test Geospatial Integrity
def test_geospatial_data():
    conn = psycopg2.connect(
        dbname="financial_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Check for valid geolocations
    cursor.execute("""
        SELECT COUNT(*) AS invalid_geolocation
        FROM transactions
        WHERE NOT ST_IsValid(ST_SetSRID(ST_MakePoint(longitude, latitude), 4326));
    """)
    assert cursor.fetchone()[0] == 0, "Invalid geospatial data found"

    conn.close()

