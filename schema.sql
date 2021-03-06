CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(80), 
	password VARCHAR(80), 
	PRIMARY KEY (id)
);
CREATE TABLE regions (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	PRIMARY KEY (id)
);
CREATE TABLE destinations (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	Visa_requirements VARCHAR(60), 
	Allowed_stay VARCHAR(80),     
	budget VARCHAR(80), 
	vaccines VARCHAR(150), 
	airport VARCHAR(100), 
	price INTEGER, 
	time_of_flight VARCHAR(80), 
	region_id INTEGER, 
	PRIMARY KEY (id),
	FOREIGN KEY (region_id) REFERENCES regions(id)
);
