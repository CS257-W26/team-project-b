DROP TABLE IF EXISTS years,countries,co2,energy,co2_data;
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
    population TEXT,
    gdp TEXT,
    cement_co2 FLOAT,
    co2 FLOAT,
    co2_growth_abs FLOAT,
    co2_including_luc FLOAT,
    co2_per_capita FLOAT,
    co2_per_gdp FLOAT,
    co2_per_unit_energy FLOAT,
    coal_co2 FLOAT,
    consumption_co2 FLOAT,
    cumulative_co2 FLOAT,
    flaring_co2 FLOAT,
    gas_co2 FLOAT,
    land_use_change_co2 FLOAT,
    methane FLOAT,
    nitrous_oxide FLOAT,
    oil_co2 FLOAT,
    other_industry_co2 FLOAT
);