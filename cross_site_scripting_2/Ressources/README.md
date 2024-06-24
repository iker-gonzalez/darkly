# Cross Site Scripting (XSS) 2

## Overview

Cross-Site Scripting (XSS) is a common web vulnerability where attackers inject malicious scripts into web pages viewed by other users. This occurs when web applications fail to properly validate or sanitize user input, allowing attackers to insert scripts that are executed in the context of other users' browsers.

XSS attacks can have various consequences, including stealing session cookies, redirecting users to malicious websites, or modifying the content of the page.

## Vulnerability Path

**http://<ip_address>/index.php?page=media&src=nsa**

## Discovery

## How It's Usually Found

1. **Automated Scanning Tools**: Attackers utilize automated tools such as vulnerability scanners or web application security scanners to detect potential XSS vulnerabilities. These tools systematically crawl through web pages, input various payloads, and analyze responses to identify points where input is not properly sanitized.

2. **Manual Testing**: Skilled attackers manually inspect the source code and behavior of web applications to uncover XSS vulnerabilities. They scrutinize forms, URLs, and JavaScript functions for potential injection points, looking for opportunities to insert malicious scripts.

3. **Reconnaissance**: Attackers conduct reconnaissance activities to gather information about the target web application. This may involve analyzing public-facing components, reviewing documentation, or studying past security advisories related to the technology stack used. Such reconnaissance helps identify common XSS vulnerabilities and potential attack vectors.

4. **Bug Bounty Programs**: Some attackers participate in bug bounty programs offered by organizations to discover and report security vulnerabilities in their web applications. XSS vulnerabilities are frequently discovered in these programs, and attackers actively search for them to earn rewards.

5. **Exploiting Known Vulnerabilities**: Attackers exploit known XSS vulnerabilities documented in public databases or security advisories. They target web applications that haven't applied patches or updates to address these vulnerabilities, leveraging them for malicious purposes.

In summary, attackers employ a combination of automated tools, manual techniques, and reconnaissance to uncover XSS vulnerabilities in web applications.

### How I Discovered It

In the main page, go to the NSA photo and change the `src` parameter in the URL to one you create. You need to replace `nsa` with `data:text/html;base64,` followed by a script encoded in base64, for example: `<script>alert("hi!");</script>`

## Additional Resources

- [BASE64 encoding web](https://www.base64encode.org/)

- [OWASP Cross-Site Scripting (XSS) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html): A comprehensive guide by OWASP on preventing XSS attacks, including techniques and best practices.

- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security): Mozilla's guidelines on web security, covering various topics including XSS prevention and mitigation strategies.

- [Google Web Fundamentals - Security Overview](https://developers.google.com/web/fundamentals/security): Google's overview of web security fundamentals, offering insights into XSS prevention and other security measures for web applications.
