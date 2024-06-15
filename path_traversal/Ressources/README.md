# Path Traversal Breach

## Overview

This document outlines a security breach involving a path traversal vulnerability discovered in a web application. Path traversal vulnerabilities allow attackers to access files on a server's filesystem that are not intended to be accessible through the web application. This can lead to unauthorized disclosure of sensitive information.

## Vulnerability Path
**http://<ip_address>/?page=../../../../../../../etc/passwd**

## Discovery

### How It's Usually Found

Path traversal vulnerabilities are typically discovered through manual testing or automated scanning tools that attempt to access files beyond the web application's root directory by manipulating input parameters.

### How I Have Discovered It

In our investigation, we utilized path traversal techniques on the webpage accessible via the affected URL. By manipulating the `page` parameter in the URL, we were able to traverse the directory structure and access sensitive files, including the `/etc/passwd` file, which contains user account information.

The vulnerability was discovered using a Python script named `path_traversal.py`. This script automates the process of exploiting the path traversal vulnerability by manipulating the `page` parameter in the URL. It attempts to access the `/etc/passwd` file by incrementally adding directory traversal sequences (`../`) to the base URL:

```bash
python3 path_traversal.py http://127.0.0.1:8080
```

The script output is as follows:

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

The script successfully accessed the `/etc/passwd` file in path **http://<ip_address>/?page=../../../../../../../etc/passwd**, revealing sensitive information about the server's user accounts:

## Prevention

To prevent path traversal vulnerabilities, consider the following measures:

1. **Input Validation:** Ensure that the application validates and sanitizes all user input to prevent malicious data from being processed.
2. **Use of Whitelists:** Implement whitelisting of allowed files and directories that can be accessed through user input parameters.
3. **Limit File Access:** Restrict the web application's access to the filesystem to only those directories and files that are necessary for its operation.
4. **Use Secure File Access APIs:** Utilize secure APIs that are designed to safely access files without exposing the underlying filesystem structure.
5. **Regular Security Audits:** Conduct regular security audits and vulnerability assessments to identify and mitigate potential vulnerabilities.

## Additional Resources

For more information on path traversal vulnerabilities and how to prevent them, refer to the following resources:

- [PortSwigger - File Path Traversal](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/path-traversal-apprentice/file-path-traversal/reading-arbitrary-files-via-path-traversal)
- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP Cheat Sheet Series - File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) (Provides insights on secure file upload, which is closely related to preventing path traversal attacks)
- [OWASP Testing Guide v4 - File System](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/06-Testing_for_Path_Traversal) (Offers a comprehensive guide on testing for path traversal vulnerabilities)