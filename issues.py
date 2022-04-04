from jira import fetch_data
import datetime
import os
import boto3
import json
from dotenv import load_dotenv

load_dotenv()



s3 = boto3.client('s3')

def load_issue():
    
    startAt = 0
    maxResults = 50
    issue_data = []

    # getting year, month, and day from the date
    date = datetime.datetime.now()
    
    day = date.strftime('%d')
    month = date.strftime('%m')
    year = date.year

    # bucket
    bucket = os.getenv("BUCKET")

    # fecthing the result from jira
    data = fetch_data(startAt, maxResults)

    total = data["total"]

    issues = data["issues"]

    for issue in issues:
        issue_key = issue["key"]
        issue_data.append(issue_key)
        print(f"{issue_key} is stored in S3 bucket {bucket}")
        # store issue in s3 bucket
        key = f"{year}/{month}/{day}/issues/{issue_key}.json"
        body = json.dumps(issue)

        s3.put_object(Bucket = bucket, Key = key, Body = body)

        
    while (len(issue_data) < total):
        startAt += maxResults
        # fecthing the result from jira
        data = fetch_data(startAt, maxResults)

        issues = data["issues"]

        for issue in issues:
            issue_key = issue["key"]
            issue_data.append(issue_key)
            print(f"{issue_key} is stored in S3 bucket {bucket}")
            # store issue in s3 bucket
            key = f"{year}/{month}/{day}/issues/{issue_key}.json"
            body = json.dumps(issue)

            s3.put_object(Bucket = bucket, Key = key, Body = body)
     
    return len(issue_data)
      