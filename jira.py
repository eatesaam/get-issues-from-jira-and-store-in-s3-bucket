import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data(startAt, maxResults):

    jira_url = os.getenv('JIRA_API_URL')
    jql = os.getenv('JQL')

    url = f"{jira_url}/rest/api/3/search/?jql={jql}"

    email = os.getenv('EMAIL')
    api_key = os.getenv('API_TOKEN')

    auth = HTTPBasicAuth(email, api_key)
    
    headers = { "Accept": "application/json"}

    query = {
        'startAt': str(startAt),
        'maxResults': str(maxResults)    
    }

    response = requests.request(
    "GET",
    url=url,
    headers=headers,
    params=query,
    auth=auth
    )

    data=response.json()

    return data
