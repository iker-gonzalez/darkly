# Hidden Credentials

## Overview

The security breach involved an `htpasswd` file that was improperly protected, allowing unauthorized access to admin credentials, ultimately leading to a compromise of the admin panel.

## Vulnerability Path
**http://<ip_address>:<port>/whatever/htpasswd**

## Discovery

## How It's Usually Found

Security breaches involving `htpasswd` files are often discovered through:

- Examination of `robots.txt` files, which may reveal hidden directories.
- Brute-forcing common directory paths to locate unsecured sensitive files.
- Google searches of exposed hashes to identify weak passwords.

## How I Discovered It

In this specific case, the breach was discovered by:

1. Inspecting the `robots.txt` file, which contained the following entries:

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

2. Exploring the `/whatever` directory, where an `htpasswd` file was found and downloaded. This file contained:

```
root:437394baff5aa33daa618be47b75cb49
```

3. Googling a [md5 hash to plain text converter](https://md5.gromweb.com/), the hash revealed it as the MD5 hash of `qwerty123@`.

4. Navigating to the `/admin` path, a common route for admin panels, where an authentication form was found. Using the credentials `root` and `qwerty123@`, I successfully logged in and gained access to the admin panel.

# Prevention

To prevent such breaches, consider the following measures:

1. **Use Stronger Passwords:**
- Implement complex passwords that are resistant to brute-force attacks.
- Avoid using common words or easily guessable phrases.

2. **Secure Directory Access:**
- Configure the web server to restrict access to sensitive files and directories.
- Ensure `.htpasswd` files are not accessible from the web.

3. **Regular Security Audits:**
- Conduct regular audits to identify and fix potential security vulnerabilities.
- Check for exposed sensitive files and insecure configurations.

4. **Encrypt Passwords Properly:**
- Use stronger hashing algorithms like bcrypt or Argon2 instead of MD5.
- Regularly update and rotate passwords and hashes.

5. **Improve Nginx Configuration:**
- Strengthen Nginx settings to prevent unauthorized file access.
- Properly configure Nginx to utilize `.htpasswd` files for authentication.

# Additional Resources

For further information about protecting against similar vulnerabilities, consider these resources:

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Nginx Security Hardening Guide](https://www.nginx.com/blog/10-tips-for-10x-application-performance-and-security/)
- [Understanding and Preventing Directory Traversal Attacks](https://owasp.org/www-community/attacks/Path_Traversal)
- [Properly Using .htpasswd with Apache](https://httpd.apache.org/docs/2.4/howto/auth.html)
- [Best Practices for Secure Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
