-- Create the table if it does not exist

CREATE TABLE IF NOT EXISTS second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

-- Insert the specified records
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
