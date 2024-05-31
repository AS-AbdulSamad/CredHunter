# CredHunter

CredHunter is a command-line tool designed to quickly search for potentially sensitive keywords within a list of URLs. It helps security professionals and developers identify URLs that may contain credentials, API keys, or other sensitive information, facilitating proactive security measures and risk mitigation.

##Features:

1. **Efficient Keyword Matching:** Utilizes regular expressions for fast and accurate matching of keywords within URLs.
2. **Grouped Results:** Organizes matched URLs by keyword, providing a clear overview of potential vulnerabilities.
3. **Customizable Keywords:** Allows users to easily define and customize the list of keywords to match specific use cases or environments.
4. **Simple Integration:** Run as a standalone Python script, making it easy to integrate into existing workflows or automation pipelines.

##Usage:

* Create a text file containing a list of URLs.
* Run the CredHunter.py script with the path to the URL file as an argument. Example: Python3 CredHunter.py urls.txt
* View the matched URLs grouped by keyword.

CredHunter is a valuable tool for penetration testers, enabling them to conduct comprehensive security assessments and identify potential security weaknesses related to exposed credentials or sensitive information in URLs.
