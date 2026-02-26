DROP TABLE IF EXISTS co2_data,energy_data;

CREATE TABLE co2_data (
    country TEXT,
    year INTEGER,
    iso_code TEXT,
    population BIGINT,
    co2 FLOAT,
    co2_per_capita FLOAT
);

CREATE TABLE energy_data (
    country TEXT,
    year INTEGER,
    iso_code TEXT,
    population BIGINT,
    biofuel_electricity FLOAT,
    energy_per_capita FLOAT,
    gas_electricity FLOAT
);