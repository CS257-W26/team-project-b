DROP TABLE IF EXISTS years,countries,co2,energy,co2_data,energy_data;
CREATE TABLE years (
    id SERIAL,
    year INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE countries(
    id SERIAL,
    country TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE co2 (
    id SERIAL,
    co2_per_capita FLOAT,
    cummulative_co2 FLOAT,
    PRIMARY KEY (id)
);

CREATE TABLE energy (
    id SERIAL,
    biofuel_cons_per_capita FLOAT,
    PRIMARY KEY (id)
);

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