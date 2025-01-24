# Deep Dive: Financial Transaction Analysis

## Objective
This project provides a robust and efficient data model for managing and analyzing financial transactions in a banking or fintech application. The focus is on customer account management, transaction tracking, fraud detection, and analytics. It incorporates PostgreSQL, PostGIS, Python, Faker for data generation, and Tableau for visualization.

---

## Features
### Core Functionalities
1. **Customer Management**
   - Store customer details: name, address, contact info, account types.
   - Fields for compliance (e.g., KYC status, risk profile).

2. **Account Management**
   - Support multiple account types (e.g., checking, savings, credit).
   - Track balances, overdraft limits, and account statuses (active/closed).

3. **Transaction Logging**
   - Detailed data: Transaction ID, timestamp, amount, type (credit/debit), and status.
   - Geolocation data for fraud detection.

4. **Fraud Detection**
   - Velocity checks (rapid transaction frequency).
   - Geospatial analysis for location anomalies.
   - Threshold-based flagging for suspicious amounts.

5. **Analytics**
   - Insights like total deposits/withdrawals, high-risk account activity, and monthly metrics.

---

## Project Components

### 1. **Database Schema (PostgreSQL with PostGIS)**
The database schema is defined to support all the core functionalities. Key tables include:

- **Customers**: Stores customer details.
- **Accounts**: Tracks account balances and types.
- **Transactions**: Logs financial transactions with geolocation data.
- **Fraud Alerts**: Flags transactions that meet suspicious criteria.



### 3. **Fraud Detection Queries**

```sql
-- Transactions from high-risk countries
SELECT * FROM transactions
WHERE country_code IN ('XYZ', 'ABC');

-- Transactions at unusual hours
SELECT * FROM transactions
WHERE EXTRACT(HOUR FROM timestamp) NOT BETWEEN 6 AND 22;

-- Velocity checks: Transactions within a short period
SELECT account_id, COUNT(*) as transaction_count
FROM transactions
WHERE timestamp > NOW() - INTERVAL '1 HOUR'
GROUP BY account_id
HAVING COUNT(*) > 5;

-- Flag transactions below reporting thresholds
SELECT * FROM transactions
WHERE amount BETWEEN 9900 AND 10000;
```

### 4. **Tableau Dashboard**
- **Visualizations**:
  1. Transaction trends over time.
  2. Heatmaps of transaction locations.
  3. Fraud detection indicators.

### 5. **Docker Compose**
The project is containerized using Docker Compose for seamless deployment.



## File Structure
```
financial-transaction-analysis/  
├── data_model/  
│   ├── erd.png (ER Diagram)  
│   ├── schemas.sql (DDL for database schemas)  
│   └── data_populate.py (Script to generate data)  
├── analysis/  
│   ├── tableau/  
│   │   ├── dashboards.twb (Tableau workbook)  
│   ├── analytics_queries.sql  
├── tests/  
│   ├── test_data_integrity.py  
│   └── test_fraud_logic.py  
├── docker-compose.yml (Postgres & PostGIS setup)  
├── README.md  
└── requirements.txt  

```




---

## How to Run
1. Clone the repository.
2. Start Docker Compose: `docker-compose up -d`.
3. Execute SQL scripts to set up the schema.
4. Run the Python script to populate data: `python python/populate_data.py`.
5. Use Tableau to connect to the database and load the dashboard.





