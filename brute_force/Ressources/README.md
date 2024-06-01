# Brute Force Attack

## Vulnerability Path
**http://<ip_address>/?page=signin**

## Overview

A brute force attack is a cybersecurity technique used to gain unauthorized access to a system by trying every possible combination of usernames and passwords until the correct one is found. This method relies on the sheer force of computing power to systematically check all possible combinations.

The login credentials exposed are the following:

- **Username:** admin
- **Password:** shadow

## Conducting a Brute Force Attack

### Traditional Approach
1. Obtain a list of common usernames and passwords.
2. Write a script or use automated tools to repeatedly attempt to log in to the target system, using different username-password combinations.
3. Keep trying until a successful login is achieved or until all combinations have been exhausted.

### Using the Provided Script
1. Ensure you have a list of common usernames and passwords in text files (`common_usernames.txt` and `common_passwords.txt`).
2. Modify the script to use the target system's login page URL.
3. Run the script, which will iterate through each combination of usernames and passwords, attempting to log in.
4. If successful, the script will print the credentials used to log in and, if applicable, any discovered flag content.

## Prevention Measures

### 1. Strong Password Policies
Implement strong password policies that require users to create complex passwords with a mix of uppercase and lowercase letters, numbers, and special characters.

### 2. Account Lockout Policies
Implement account lockout policies that temporarily lock user accounts after a certain number of failed login attempts, preventing brute force attacks.

### 3. CAPTCHA
Use CAPTCHA challenges to verify that the login attempts are made by humans and not automated scripts.

### 4. Two-Factor Authentication (2FA)
Implement two-factor authentication to add an extra layer of security, requiring users to provide a second form of verification in addition to their password.

## Additional Resources

- [OWASP Brute Force Attack Prevention](https://owasp.org/www-community/attacks/Brute_force_attack)
- [NIST Guidelines for Password Policy](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Google CAPTCHA Documentation](https://developers.google.com/recaptcha)
