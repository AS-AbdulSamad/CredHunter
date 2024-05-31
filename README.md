# CredHunter

CredHunter is a command-line tool designed to aid penetration testers in quickly identifying potential security risks by searching for sensitive keywords within a list of URLs. It assists in uncovering URLs that may contain credentials, API keys, or other sensitive information, enabling penetration testers to perform thorough security assessments and identify potential attack vectors.

## Features:

1. **Efficient Keyword Matching:** Utilizes regular expressions for fast and accurate matching of keywords within URLs.
2. **Grouped Results:** Organizes matched URLs by keyword, providing a clear overview of potential vulnerabilities.
3. **Customizable Keywords:** Allows users to easily define and customize the list of keywords to match specific use cases or environments.
4. **Simple Integration:** Run as a standalone Python script, making it easy to integrate into existing workflows or automation pipelines.

## Usage:

* Create a text file containing a list of URLs.
* Run the CredHunter.py script with the path to the URL file as an argument. Example: Python3 CredHunter.py urls.txt
* View the matched URLs grouped by keyword.

## Sample

![image](https://github.com/AS-AbdulSamad/CredHunter/assets/116205223/36ff18f0-70a1-4c07-a59f-26a68b825447)

## Disclaimer:

CredHunter is a tool developed by ABStronics for informational and educational purposes only. While CredHunter aims to assist users in identifying potential security risks, it is ultimately the responsibility of the user to ensure the security of their systems and networks. ABStronics does not guarantee the accuracy, completeness, or effectiveness of CredHunter in detecting vulnerabilities or mitigating security threats. By using CredHunter, you agree that ABStronics shall not be liable for any damages or losses arising from the use or misuse of this tool.
