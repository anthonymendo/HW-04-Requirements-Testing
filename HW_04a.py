import json
import requests
import unittest

def github_parser(user_ID):
    url = "https://api.github.com/users/" + user_ID + "/repos"
    url_json = json.loads(requests.get(url).text)

    if type(url_json)==dict and url_json['message']=='Not Found':
        output_msg = "Repository not found"
        print(output_msg)
        return output_msg

    store = []

    for repo in url_json:
        repo_name = repo['name']
        commits_url = repo['commits_url'].split("{/sha}")[0]
        commits_json = json.loads(requests.get(commits_url).text)
        total_commits = len(commits_json)
        x = "Repository Name: " + repo_name  + " Number of commits: " + str(total_commits)
        print(x)
        store.append(x)

    return store

    #github_parser('')