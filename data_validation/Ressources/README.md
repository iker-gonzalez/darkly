# Data Validation Input Vulnerability

# Overview
Data Validation Input Vulnerability is a common security issue in web applications where user input is not properly validated or sanitized. This vulnerability allows attackers to manipulate the input data in ways that can compromise the security or stability of the application. It can lead to various security risks, including unauthorized data access, data corruption, and application crashes.

This type of vulnerability is particularly concerning in applications that rely on user input to perform critical operations, such as database queries, file operations, or conditional logic. Without proper validation, attackers can supply unexpected values that exploit the logic of the application.

## Vulnerability Path
**http://<ip_address>/survey.php?question=1&option=99**

## Discovery

## How It's Usually Found

1. **Automated Scanning Tools**: Security professionals and attackers use automated tools to detect input validation vulnerabilities. These tools test web applications by submitting a wide range of unexpected or malicious inputs to various fields and observing the application's response.

2. **Manual Testing**: Through manual testing, individuals can discover input validation issues by experimenting with different inputs to see if the application behaves unexpectedly. This often involves trying to bypass client-side validation or entering values that are outside the expected range.

3. **Code Review**: A thorough review of the application's source code can reveal areas where input validation is missing or improperly implemented. Developers look for functions that process user input without checking its validity.

4. **Penetration Testing**: Penetration testers simulate attacks against the application to identify vulnerabilities, including input validation issues. They use a combination of manual techniques and automated tools to uncover weaknesses that could be exploited.

5. **User Feedback**: Sometimes, users inadvertently discover input validation vulnerabilities during normal use of the application. They might report unusual behavior after entering specific types of data, which can lead to the discovery of a vulnerability.

### How I Discovered It
While participating in a survey on the application, I noticed that the select options for a question were client-side validated. By inspecting the element and modifying the value of an option to a number greater than 10, which was outside the expected range, I was able to submit the form with this invalid data. This indicated a lack of proper server-side data validation.

## Additional Resources

- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html): A comprehensive guide by OWASP on input validation, including techniques and best practices for validating user input.

- [Mozilla Developer Network - Form data validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation): Mozilla's guide on implementing form data validation, covering both client-side and server-side validation strategies.

- [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security): Google's overview of web security fundamentals, with a section on validating and sanitizing data.