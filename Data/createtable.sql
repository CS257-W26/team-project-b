DROP IF EXISTS years;
CREATE TABLE years (
    id SERIAL,
    years INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE co2 (
    country TEXT,
    
    co2_capita INTEGER,
    
    FOREIGN KEY (years_id)
)

CREATE TABLE 