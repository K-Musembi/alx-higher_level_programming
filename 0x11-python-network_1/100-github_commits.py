#!/usr/bin/python3
'''Last ten commits from GitHub
'''

import requests
import sys


repo_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

parameters = {'per_page': 10}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        sha = commits['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    pass
