-- Proj: djseri

-- Show current db
SELECT current_database();

--CREATE DATABASE djseri_db;


SELECT * FROM employees ORDER BY id DESC;


SELECT column_name, data_type, character_maximum_length
FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'customers';
