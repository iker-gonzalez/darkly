# Sensitive Directory Disclosure

## Overview

The `sensitive-directory-disclosure` vulnerability arises when sensitive directories or files are exposed on a web server but are intended to be hidden. Attackers can exploit this by locating and accessing these hidden directories, potentially leading to data leaks or unauthorized access to sensitive information.

## Vulnerability Path

**http://<ip_address>/.hidden/**

## Discovery

### How It's Usually Conducted

- **Web crawling and directory enumeration:** Automated tools like Dirbuster, Gobuster, or DirB are used to systematically scan websites for hidden directories and files. These tools try accessing various common directory names and file paths to discover unintentionally exposed resources.

- **Analysis of robots.txt and sitemap files:** Examining the robots.txt file and XML sitemaps can reveal directories or files that site owners intended to keep private but inadvertently disclosed.

- **Source code review:** Inspecting the HTML source code of web pages, JavaScript files, and other client-side resources can sometimes reveal references to hidden directories or sensitive file paths that weren't meant to be publicly accessible.

### How I Discovered It

During our investigation, we saw in the `robots.txt` that the directory `/.hidden` was exposed. Given its name, we suspected it might contain sensitive information. Upon navigating to that directory, we discovered it contained a maze of endless subdirectories, ultimately leading to some `README` files. To efficiently search for sensitive information in these files, we developed a script with the following functionality:

- **Web Scraping**: The script utilizes the `requests` library to send GET requests to web pages and `BeautifulSoup` to parse the HTML content. It begins from a root address and recursively explores directories, focusing on the `.hidden/` directory.

- **Link Traversal**: For each page, the script extracts all links using BeautifulSoup. It then recursively visits each link that isn't pointing to a parent directory ("../"), effectively exploring the entire directory structure.

- **README File Processing**: When a `README` file is encountered, the `print_file_content` function is called. This function checks if the file's content contains the word "flag". If found, it prints the content in green and exits the script.

- **Error Handling and User Interface**: The script includes basic error handling for network requests and provides a simple command-line interface, expecting an IP address as an argument. It also uses color coding (green) to highlight when the flag is found.

## Additional Resources

- [OWASP: Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [OWASP: Forced Browsing](https://owasp.org/www-community/attacks/Forced_browsing)
- [OWASP: Testing for Directory Traversal/File Include](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include)
- [CWE-538: Insertion of Sensitive Information into Externally-Accessible File or Directory](https://cwe.mitre.org/data/definitions/538.html)
- [NIST: Hidden File and Directory Discovery](https://nvd.nist.gov/vuln/detail/CVE-2020-35489)
