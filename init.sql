CREATE TABLE IF NOT EXISTS wind_data_bronze (
    id SERIAL PRIMARY KEY,
    winddirabs NUMERIC
);

CREATE TABLE IF NOT EXISTS wind_data_silver (
    id SERIAL PRIMARY KEY,
    winddirabs NUMERIC
);

CREATE TABLE IF NOT EXISTS wind_data_gold (
    id SERIAL PRIMARY KEY,
    avg_winddirabs NUMERIC,
    calculated_at TIMESTAMP
);
