# Hidden Fields in Submit Forms Vulnerability

## Overview

Hidden fields in submit forms vulnerability occurs when sensitive information is included in the HTML code of a form but is not visible to the user. Attackers can exploit this vulnerability to manipulate or submit unauthorized data to the server.

## Discovery

### How It's Usually Found
Hidden fields in submit forms are typically discovered during web application security assessments or penetration testing. Security professionals inspect the HTML source code of web pages to identify any hidden fields that may contain sensitive information or be vulnerable to manipulation.

### How I Discovered It
I discovered this vulnerability by inspecting the HTML code of the form page. Upon examination, I found hidden fields containing sensitive data such as authentication tokens or session identifiers. This exposed the application to potential exploitation by attackers.


## Prevention

To prevent hidden fields in submit forms vulnerability, follow these best practices:

1. **Avoid Storing Sensitive Data**: Do not store sensitive information in hidden form fields. Instead, use server-side session management or secure cookies to maintain user state.

2. **Validate Input**: Implement strict input validation to ensure that only expected and valid data is submitted through forms.

3. **Use Encryption**: Encrypt sensitive data before transmitting it to the client, and decrypt it securely on the server side.

4. **Implement CSRF Protection**: Use techniques such as CSRF tokens to protect against cross-site request forgery attacks, which can exploit hidden form fields.

5. **Secure Coding Practices**: Follow secure coding practices and regularly audit your codebase for vulnerabilities.

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Security Academy](https://portswigger.net/web-security)
- [HTML Forms Guide](https://www.w3schools.com/html/html_forms.asp)
