# Path Traversal Breach

## Overview

This document outlines a security breach involving a path traversal vulnerability discovered in a web application. Path traversal vulnerabilities allow attackers to access files on a server's filesystem that are not intended to be accessible through the web application. This can lead to unauthorized disclosure of sensitive information.

## Vulnerability Path
**http://<ip_address>/?page=../../../../../../../etc/passwd**

## Discovery

### How It's Usually Found

Path traversal vulnerabilities are typically discovered through manual testing or automated scanning tools that attempt to access files beyond the web application's root directory by manipulating input parameters.

### How I Have Discovered It

During our investigation, we employed path traversal methods on a webpage accessible through a specific URL. By altering the `page` parameter in the URL, we managed to navigate through the directory structure and access confidential files, including the `/etc/passwd` file. This file, common in Unix and Linux systems, holds basic user attributes such as user ID, group ID, home directory, and shell, and is used by various system utilities to map user IDs to usernames.

The `/etc/passwd` file, targeted by the script through a path traversal vulnerability, can hold sensitive data. Although it doesn't store passwords, it does list all user accounts on the system, along with some account information (like user ID, group ID, home directory, and shell). An attacker could potentially use this information to gain a deeper understanding of the system and facilitate further attacks.

We discovered the vulnerability using a Python script named `path_traversal.py`. This script automates the process of exploiting the path traversal vulnerability by manipulating the `page` parameter in the URL. It tries to access the `/etc/passwd` file by progressively adding directory traversal sequences (`../`) to the base URL:

```bash
python3 path_traversal.py http://127.0.0.1:8080
```

The script's output is as follows:

```plaintext
http://127.0.0.1:8080/?page=etc/passwd
http://127.0.0.1:8080/?page=../etc/passwd
http://127.0.0.1:8080/?page=../../etc/passwd
http://127.0.0.1:8080/?page=../../../etc/passwd
http://127.0.0.1:8080/?page=../../../../etc/passwd
http://127.0.0.1:8080/?page=../../../../../etc/passwd
http://127.0.0.1:8080/?page=../../../../../../etc/passwd
http://127.0.0.1:8080/?page=../../../../../../../etc/passwd
FOUND
```

The script successfully accessed the `/etc/passwd` file at the path **http://<ip_address>/?page=../../../../../../../etc/passwd**, exposing sensitive information about the server's user accounts. Here are more common sensitive file paths in Unix/Linux-based systems that could be exploited with this script:

1. `/etc/shadow`: Contains encrypted password and other information such as password expiration for each user.

2. `/etc/group`: Contains group membership information.

3. `/etc/sudoers`: Defines which users can run what software on which machines and as which users.

4. `/etc/ssh/sshd_config`: Contains configurations for the SSH daemon, including what users are allowed to log in.

5. `/etc/ssh/ssh_config`: Contains client-side configurations for SSH, including the system-wide configuration for every SSH client on the system.

6. `/root/.ssh/id_rsa`: Contains the private key for the root user (if it exists).

7. `/home/*/.ssh/id_rsa`: Contains private keys for any user that has one.

8. `/var/log/auth.log` or `/var/log/secure`: Contains system log messages related to authentication and authorization.

9. `/etc/mysql/my.cnf`: Contains MySQL configuration, including possibly passwords.

10. `/proc/self/environ`: Contains environment variables.

## Prevention

To prevent path traversal vulnerabilities, consider the following measures:

1. **Input Validation:** Ensure that the application validates and sanitizes all user input to prevent malicious data from being processed.
2. **Use of Whitelists:** Implement whitelisting of allowed files and directories that can be accessed through user input parameters.
3. **Limit File Access:** Restrict the web application's access to the filesystem to only those directories and files that are necessary for its operation.
4. **Use Secure File Access APIs:** Utilize secure APIs that are designed to safely access files without exposing the underlying filesystem structure.
5. **Regular Security Audits:** Conduct regular security audits and vulnerability assessments to identify and mitigate potential vulnerabilities.

## Additional Resources

For more information on path traversal vulnerabilities and how to prevent them, refer to the following resources:

- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP Cheat Sheet Series - File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) (Provides insights on secure file upload, which is closely related to preventing path traversal attacks)
