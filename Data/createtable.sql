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

CREATE TABLE energy_data (
    country TEXT,
    year INTEGER,
    iso_code TEXT,
    population BIGINT,
    gdp TEXT,
    biofuel_cons_per_capita FLOAT,
    biofuel_consumption FLOAT,
    biofuel_elec_per_capita FLOAT,
    biofuel_electricity FLOAT,
    coal_elec_per_capita FLOAT,
    coal_electricity FLOAT,
    electricity_generation FLOAT,
    electricity_share_energy FLOAT,
    energy_per_capita FLOAT,
    fossil_electricity FLOAT,
    gas_electricity FLOAT,
    gas_energy_per_capita FLOAT,
    hydro_elec_per_capita FLOAT,
    hydro_electricity FLOAT,
    hydro_energy_per_capita FLOAT,
    nuclear_elec_per_capita FLOAT,
    nuclear_electricity FLOAT,
    nuclear_energy_per_capita FLOAT,
    oil_elec_per_capita FLOAT,
    oil_electricity FLOAT,
    oil_energy_per_capita FLOAT,
    per_capita_electricity FLOAT,
    renewables_elec_per_capita FLOAT,
    renewables_electricity FLOAT,
    renewables_energy_per_capita FLOAT,
    solar_elec_per_capita FLOAT,
    solar_electricity FLOAT,
    solar_energy_per_capita FLOAT,
    wind_elec_per_capita FLOAT,
    wind_electricity FLOAT,
    wind_energy_per_capita FLOAT
);