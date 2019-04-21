/* drop tables */
DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS comment;

/* drop indexes */
DROP INDEX IF EXISTS city_region_id_idx;
DROP INDEX IF EXISTS comment_city_id_idx;

/* create region table */
CREATE TABLE region (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(255) NOT NULL
);

/* create city table */
CREATE TABLE city (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(255) NOT NULL,
    region_id INTEGER NOT NULL,
    CONSTRAINT fk_regions
        FOREIGN KEY (region_id)
        REFERENCES region(id)
        ON DELETE CASCADE
);

/* create index on foreign key city(region_id) */
CREATE INDEX city_region_id_idx ON city(region_id);

/* create comment table */
CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name varchar(255) NOT NULL,
    second_name varchar(255) NULL, -- comment goes here
    last_name varchar(255) NOT NULL,
    phone varchar(255) NULL,
    email varchar(255) NULL,
    comment text NOT NULL,
    city_id INTEGER NOT NULL,
    CONSTRAINT fk_cities
        FOREIGN KEY (city_id)
        REFERENCES city(id)
        ON DELETE CASCADE
);

/* create index on foreign key comment(city_id) */
CREATE INDEX comment_city_id_idx ON comment(city_id);

/* fixtures */
INSERT INTO region(id, name) VALUES (1, 'Краснодарский край'), (2, 'Ростовская область'), (3, 'Ставропольский край');
INSERT INTO city(name, region_id) VALUES ('Краснодар', 1), ('Кропоткин', 1), ('Славянск', 1),
                                         ('Ростов', 2), ('Шахты', 2), ('Батайск', 2),
                                         ('Ставрополь', 3), ('Пятигорск', 3), ('Кисловодск', 3);
