# CredHunter

CredHunter is a command-line tool designed to quickly search for potentially sensitive credentails within a list of URLs. It helps security professionals and developers identify URLs that may contain credentials, API keys, or other sensitive information, facilitating proactive security measures and risk mitigation.

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

![image](https://github.com/AS-AbdulSamad/CredHunter/assets/116205223/b931d1fb-bbb2-4789-bbc5-5ea2f8352b6d)

## Disclaimer:

CredHunter is a tool developed by ABStronics for informational and educational purposes only. While CredHunter aims to assist users in identifying potential security risks, it is ultimately the responsibility of the user to ensure the security of their systems and networks. ABStronics does not guarantee the accuracy, completeness, or effectiveness of CredHunter in detecting vulnerabilities or mitigating security threats. By using CredHunter, you agree that ABStronics shall not be liable for any damages or losses arising from the use or misuse of this tool.
