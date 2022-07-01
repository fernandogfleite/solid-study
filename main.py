from github.client import GithubClient
from repo.parse import RepoParse


if __name__ == "__main__":
    username = "fernandogfleite"
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        RepoParse.parse(response['body'])
    
    else:
        print(response['body'])
