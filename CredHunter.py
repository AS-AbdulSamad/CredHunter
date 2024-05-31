#! /usr/bin/python3

import re
import sys
from collections import defaultdict

def print_ascii_art():
    ascii_art = """
  ___  ____  ____  ____  _  _  _  _  __ _  ____  ____  ____ 
 / __)(  _ \(  __)(    \/ )( \/ )( \(  ( \(_  _)(  __)(  _ \\
( (__  )   / ) _)  ) D () __ () \/ (/    /  )(   ) _)  )   /
 \___)(__\_)(____)(____/\_)(_/\____/\_)__) (__) (____)(__\_)
 
 					Script By: ABStronics
 		  		Visit: https://abstronics.com
 ------------------------------------------------------------
    """
    print(ascii_art)

def main(file_path):
    # Define the keywords
    keywords = [
        "aws_access_key=", "aws_secret_key=", "api_key=", "passwd=", "pwd=", "heroku=", "slack=", "firebase=", "swagger=", "aws_key=", "password=", "ftp_password=", "jdbc=", "db=", "sql=", "secret=", "jet=", "config=", "admin=", "json=", "gcp=", "htaccess=", ".env=", "ssh_key=", ".git=", "access_key=", "secret_token=", "oauth_token=", "oauth_token_secret=", "user=", "username=", "key=", "private_key=", "client_secret=", "client_id=", "bearer_token=", "token=", "api_secret=", "root_password=", "admin_password=", "db_password=", "mongo_uri=", "redis_url=", "smtp_password=", "smtp_user=", "smtp_username=", "ftp_user=", "ssh_passphrase=", "aws_access_key_id=", "aws_secret_access_key=", "db_uri=", "auth_key=", "auth_token=", "auth_secret=", "ftp_login=", "encryption_key=", "decryption_key=", "signing_key=", "verification_key=", "connection_string=", "db_conn=", "api_key_secret=", "service_account=", "api_token=", "jwt_secret=", "api_client_secret=", "oauth_client_id=", "oauth_client_secret=", "app_secret=", "session_key=", "csrf_token=", "csrf_secret=", "webhook_url=", "webhook_secret=", "sns_topic=", "s3_bucket=", "firebase_api_key=", "google_api_key=", "google_client_id=", "google_client_secret=", "facebook_api_key=", "facebook_app_secret=", "twitter_api_key=", "twitter_api_secret=", "linkedin_client_id=", "linkedin_client_secret=", "github_client_id=", "github_client_secret=", "bitbucket_client_id=", "bitbucket_client_secret=", "heroku_api_key=", "pagerduty_api_key=", "datadog_api_key=", "splunk_api_key=", "rollbar_access_token=", "newrelic_api_key=", "newrelic_app_id=", "sentry_dsn=", "travis_token=", "circleci_token=", "aws_access_key=", "aws_secret_key=", "api key=", "passwd=", "pwd=", "heroku=", "slack=", "firebase=", "swagger=", "aws_secret_key=", "aws key=", "password=", "ftp password=", "jdbc=", "db=", "sql=", "secret jet=", "config=", "admin=", "pwd=", "json=", "gcp=", "htaccess=", ".env=", "ssh key=", ".git=", "access key=", "secret token=", "oauth_token=", "oauth_token_secret=", "user=", "name=", "aws_access_key:", "aws_secret_key:", "api_key:", "passwd:", "pwd:", "heroku:", "slack:", "firebase:", "swagger:", "aws_key:", "password:", "ftp_password:", "jdbc:", "db:", "sql:", "secret:", "jet:", "config:", "admin:", "json:", "gcp:", "htaccess:",
".env:", "ssh_key:", ".git:", "access_key:", "secret_token:", "oauth_token:", "oauth_token_secret:", "user:", "username:", "key:", "private_key:", "client_secret:", "client_id:", "bearer_token:", "token:", "api_secret:", "root_password:", "admin_password:", "db_password:", "mongo_uri:", "redis_url:", "smtp_password:", "smtp_user:", "smtp_username:", "ftp_user:", "ssh_passphrase:", "aws_access_key_id:", "aws_secret_access_key:", "db_uri:", "auth_key:", "auth_token:", "auth_secret:", "ftp_login:", "encryption_key:", "decryption_key:", "signing_key:", "verification_key:", "connection_string:", "db_conn:", "api_key_secret:", "service_account:", "api_token:", "jwt_secret:", "api_client_secret:", "oauth_client_id:", "oauth_client_secret:", "app_secret:", "session_key:", "csrf_token:", "csrf_secret:", "webhook_url:", "webhook_secret:", "sns_topic:", "s3_bucket:", "firebase_api_key:", "google_api_key:", "google_client_id:", "google_client_secret:", "facebook_api_key:", "facebook_app_secret:", "twitter_api_key:", "twitter_api_secret:", "linkedin_client_id:", "linkedin_client_secret:", "github_client_id:", "github_client_secret:", "bitbucket_client_id:", "bitbucket_client_secret:", "heroku_api_key:", "pagerduty_api_key:", "datadog_api_key:", "splunk_api_key:", "rollbar_access_token:", "newrelic_api_key:", "newrelic_app_id:", "sentry_dsn:", "travis_token:", "circleci_token:", "aws_access_key:", "aws_secret_key:", "api key:", "passwd:", "pwd:", "heroku:", "slack:", "firebase:", "swagger:", "aws_secret_key:", "aws key:", "password:", "ftp password:", "jdbc:", "db:", "sql:", "secret jet:", "config:", "admin:", "pwd:", "json:", "gcp:", "htaccess:", ".env:", "ssh key:", ".git:", "access key:", "secret token:", "oauth_token:", "oauth_token_secret:", "user:", "name:"
    ]

    # Compile regex for faster matching
    keywords_regex = re.compile("|".join([re.escape(keyword) for keyword in keywords]), re.IGNORECASE)

    # Read URLs from the specified file
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Dictionary to hold matched URLs grouped by keyword
    matched_urls = defaultdict(list)

    # Filter and print URLs that contain any of the keywords
    for url in urls:
        url = url.strip()
        for keyword in keywords:
            if re.search(re.escape(keyword), url, re.IGNORECASE):
                matched_urls[keyword].append(url)

    # Print the results grouped by keywords
    for keyword, urls in matched_urls.items():
        print(f"Keyword: {keyword}")
        for url in urls:
            print(f"    {url}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_ascii_art()
        print("Usage: python CredHunter.py <urls.txt>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print_ascii_art()
    main(file_path)
