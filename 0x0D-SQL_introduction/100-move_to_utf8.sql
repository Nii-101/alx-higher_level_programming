-- Converting the database, table(first_table) and field name to utf8
USE hbtn_0c_0
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;

SELECT CONVERT(name USING utf8) FROM first_table;
