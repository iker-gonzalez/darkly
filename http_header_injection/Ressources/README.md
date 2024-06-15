# Overview

This document outlines a security breach involving header manipulation, where unauthorized access was gained by altering the `User-Agent` and `Referer` HTTP headers. This vulnerability allows attackers to bypass security measures and access restricted areas of a web application.

## Vulnerability Path
**http://<ip_address>/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f**

## Discovery

### How It's Usually Found

Such vulnerabilities are typically discovered through code reviews, penetration testing, and the use of automated security scanning tools that identify weaknesses in handling HTTP headers.

### How I Discovered It

The vulnerability was discovered in the source code of a webpage, where a comment hinted at specific requirements for the `User-Agent` and `Referer` headers to access further functionality. By modifying these headers to meet the specified conditions, it was possible to exploit this vulnerability and gain unauthorized access.

By sending a crafted HTTP request using `curl`, the request was modified to include specific `User-Agent` and `Referer` headers that were hinted at in the application's source code. Here's the command I used:

```bash
curl -H "User-Agent: ft_bornToSec" -H "Referer: https://www.nsa.gov/" "http://127.0.0.1:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep 'flag'
```

This resulted in a response that included the flag `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`, confirming the successful exploitation of the vulnerability.

## Prevention

To prevent this type of vulnerability, consider the following measures:

1. **Validate Headers Rigorously**: Implement strict validation for all incoming HTTP headers, especially those that can influence application behavior or access control.
2. **Limit Header-Based Redirection**: Avoid relying on header values for critical application logic, such as authentication or redirection.
3. **Use Secure Coding Practices**: Follow secure coding guidelines that include checks against header injection and manipulation.
4. **Employ Web Application Firewalls (WAFs)**: Use WAFs to detect and block attempts to manipulate headers in malicious ways.
5. **Regular Security Audits**: Conduct regular security audits and penetration testing to identify and remediate vulnerabilities related to header manipulation.

## Additional Resources

For more information on mitigating vulnerabilities related to HTTP header manipulation, the following resources may be helpful:

- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [CWE-290: Authentication Bypass by Spoofing](https://cwe.mitre.org/data/definitions/290.html)