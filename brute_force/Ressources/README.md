# Brute Force Attack

## Overview

A brute force attack is a cybersecurity technique used to gain unauthorized access to a system by trying every possible combination of usernames and passwords until the correct one is found. This method relies on the sheer force of computing power to systematically check all possible combinations.

## Vulnerability Path
**http://<ip_address>/?page=signin**

## Discovery

### How It's Usually Conducted

Brute force attacks are typically conducted by cybercriminals using automated tools or scripts that systematically try every possible combination of usernames and passwords until the correct one is found. These attacks often follow a standard process:

1. **Obtain Credentials**: Attackers may obtain a list of common usernames and passwords from various sources, such as previous data breaches, publicly available databases, or automated password generation tools.

2. **Script or Tool Setup**: The attacker sets up a script or uses automated tools designed to repeatedly attempt to log in to the target system. These tools automate the process of trying different combinations of usernames and passwords.

3. **Login Attempts**: The script or tool begins the brute force attack by submitting login requests to the target system's login page, using different username-password combinations from the provided list.

4. **Systematic Iteration**: The attack systematically iterates through each combination, trying to gain access to the system. The process continues until either the correct credentials are found, or all possible combinations have been exhausted.

5. **Persistence**: In some cases, attackers may employ techniques to evade detection or bypass security measures, such as slowing down the rate of login attempts to avoid triggering account lockout policies.

Overall, brute force attacks rely on the sheer computational power and persistence of the attacker to breach the system's defenses and gain unauthorized access.

### How I Discovered It
1. I have set two files with most common usernames and passwords used (`common_usernames.txt` and `common_passwords.txt`).
2. This script will iterate through each combination of usernames and passwords, attempting to log in target signin URL:

```
http://127.0.0.1:8080/?page=signin&username={}&password={}&Login=Login#
```

3. After various attempts, the script successfully found the correct credentials:

```
- Username: admin
- Password: shadow
```

4. Using these credentials, I was able to log in to the admin panel and gain unauthorized access to sensitive information.

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
