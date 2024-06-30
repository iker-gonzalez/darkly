# Cross Site Scripting (XSS)

# Overview
Cross-Site Scripting (XSS) is a common web vulnerability where attackers inject malicious scripts into web pages viewed by other users. This occurs when web applications fail to properly validate or sanitize user input, allowing attackers to insert scripts that are executed in the context of other users' browsers. 

XSS attacks can have various consequences, including stealing session cookies, redirecting users to malicious websites, or modifying the content of the page.

## Vulnerability Path
**http://<ip_address>/index.php?page=feedback**

## Discovery

## How It's Usually Found

1. **Automated Scanning Tools**: Attackers utilize automated tools such as vulnerability scanners or web application security scanners to detect potential XSS vulnerabilities. These tools systematically crawl through web pages, input various payloads, and analyze responses to identify points where input is not properly sanitized.

2. **Manual Testing**: Skilled attackers manually inspect the source code and behavior of web applications to uncover XSS vulnerabilities. They scrutinize forms, URLs, and JavaScript functions for potential injection points, looking for opportunities to insert malicious scripts.

3. **Reconnaissance**: Attackers conduct reconnaissance activities to gather information about the target web application. This may involve analyzing public-facing components, reviewing documentation, or studying past security advisories related to the technology stack used. Such reconnaissance helps identify common XSS vulnerabilities and potential attack vectors.

4. **Bug Bounty Programs**: Some attackers participate in bug bounty programs offered by organizations to discover and report security vulnerabilities in their web applications. XSS vulnerabilities are frequently discovered in these programs, and attackers actively search for them to earn rewards.

5. **Exploiting Known Vulnerabilities**: Attackers exploit known XSS vulnerabilities documented in public databases or security advisories. They target web applications that haven't applied patches or updates to address these vulnerabilities, leveraging them for malicious purposes.

In summary, attackers employ a combination of automated tools, manual techniques, and reconnaissance to uncover XSS vulnerabilities in web applications.


### How I Discovered It
I found this vulnerability when inputing feedback through the web form existing in the vulnerability path. The following steps outline the discovery process:

- **Assumption Error**: Initially, it was assumed that submission required both the Name field and message fields to be filled (given the * mark next to both of them).

- **Form Submission**: Upon submitting the form with only the Name field filled, no error message was triggered despite of having the message section empty.

- **Source Code Inspection**: Upon inspecting the form's source code, two significant observations were made:
  1. The form invokes the `validate_form()` JavaScript function upon submission, ensuring that fields are not empty (`<form method="post" name="guestform" onsubmit="return validate_form(this)">`).
  2. The form button triggers the `checkForm()` function upon click (`<td><input name="btnSign" type="Submit" value="Sign Guestbook" onClick="return checkForm();"></td>`).

- **Error Identification**: Submitting the form resulted in a console error message indicating the absence of `checkForm()` in the source code, hence meaning that the only input validation made is the one from validate_form(), that only checks if fields name and message are empty or not. Moreover, there is a typo error in `validate_form()`: in the form, the textarea name is given as **mtxtMessage**, but in the `validate_form()` function, it's referred to as **mtxMessage**. Because of this discrepancy, the `validate_required()` function can't find the "mtxMessage" field, so it doesn't perform the validation check on the message field. As a result, the form can be submitted even if the message field is empty.

- **XSS Exploration**: Subsequently, the form was tested for Cross-Site Scripting (XSS) vulnerability by injecting a simple script into the message field, which successfully exploited the vulnerability. Additionally, it was discovered that entering "script" in either the Name or Message input fields also led to the retrieval of sensitive data.

## Prevention

1. **Input Validation**: Implement strict input validation to ensure that user-supplied data conforms to expected formats and does not contain potentially harmful scripts:

  - **Data Type Validation**: Check if the input matches the expected data type. For example, if a field is supposed to receive an email, the input should be validated against an email format.

  - **Length Validation**: Check if the input length is within the expected range. This can prevent buffer overflow attacks.

  - **Format Validation**: Check if the input matches a specific format. For example, a date field might require the input to be in the format "MM/DD/YYYY".

  - **Range Validation**: Check if a numerical input falls within a certain range.

  - **Regular Expression Validation**: Use regular expressions to enforce complex input patterns.

  - **Blacklist Validation**: Check the input against a list of known bad inputs.

  - **Whitelist Validation**: Only allow inputs that match a list of known good inputs.

  - **Encoding**: Encode user input to ensure that potentially harmful characters are not interpreted in a harmful way.

  - **Sanitization**: Remove or replace any potentially harmful characters from the input.

  Remember, client-side validation can be bypassed, so it's important to also perform **server-side validation**.
      
2. **Content Security Policy (CSP)**: Utilize CSP headers to specify which sources of content are allowed to be loaded on a web page, thereby reducing the risk of XSS attacks by limiting the execution of untrusted scripts.

3. **HTTPOnly Cookies**: Set the HTTPOnly flag on cookies to prevent client-side scripts from accessing them, thereby mitigating the risk of session hijacking via XSS attacks.

4. **Regular Security Audits and Updates**: Conduct periodic security audits of web applications to identify and patch potential XSS vulnerabilities. Stay updated with security best practices and incorporate relevant security patches and updates into the application's codebase.

## Additional Resources

- [OWASP Cross-Site Scripting (XSS) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html): A comprehensive guide by OWASP on preventing XSS attacks, including techniques and best practices.

- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security): Mozilla's guidelines on web security, covering various topics including XSS prevention and mitigation strategies.

- [Google Web Fundamentals - Security Overview](https://developers.google.com/web/fundamentals/security): Google's overview of web security fundamentals, offering insights into XSS prevention and other security measures for web applications.


