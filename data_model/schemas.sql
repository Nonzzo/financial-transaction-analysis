-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;

-- Customer table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    address TEXT,
    kyc_status BOOLEAN DEFAULT FALSE,
    risk_profile VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Account table
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    account_type VARCHAR(50) NOT NULL, -- e.g., checking, savings, credit
    balance NUMERIC(15, 2) DEFAULT 0,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(id),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount NUMERIC(15, 2) NOT NULL,
    type VARCHAR(20) NOT NULL, -- credit or debit
    status VARCHAR(20) DEFAULT 'completed',
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    country_code CHAR(3)
);

-- Fraud alerts table
CREATE TABLE fraud_alerts (
    id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES transactions(id),
    reason TEXT NOT NULL,
    flagged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'open'
);