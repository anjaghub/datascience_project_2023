import json
import requests
import numpy as np
import pandas as pd
from datetime import datetime
from abc import ABC
import sys
import time
# API Doc: https://www.reddit.com/dev/api/


class RedditScraping(ABC):
    def __init__(self, df, data_path, credentials_path, params=None) -> None:
        """ADD DOCSTRING"""
        self.df = df
        self.data_path = data_path
        self.credentials_path = credentials_path
        self.results = np.zeros(self.df.shape[0])
        self.__authenticate()
        if not params: 
            self.params = {'limit': 500}
        else: 
            self.params = params

    def __authenticate(self):
        # Load credentials data
        with open(self.credentials_path) as f:
            credentials = json.load(f)

        # Authenticate API
        client_auth = requests.auth.HTTPBasicAuth(credentials["personal_use_script"], credentials["secret"])

        credentials = {
            'grant_type': 'password',
            'username': credentials["username"],
            'password': credentials["password"]
        }
        headers = {'User-Agent': 'myBot/0.0.1'}

        # send authentication request for OAuth token
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=client_auth, data=credentials, headers=headers)
        # extract token from response and format correctly
        token = f"bearer {res.json()['access_token']}"
        # update API headers with authorization (bearer token)
        self.headers = {**headers, **{'Authorization': token}}

    def save(self, savename=None):
        if not savename:
            savename = str(datetime.now()) + "_scrapedata.csv"
        self.results.to_csv(self.data_path + savename)


class ScrapePosts(RedditScraping):
    def __init__(self, df, data_path, credentials_path, params=None) -> None:
        super().__init__(df, data_path, credentials_path, params)

    def scrape_post(self, subreddit, post_id):
        time.sleep(1)
        # FIXME include timing to not exceed rate limits; try to access http header again
        # https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds
        res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}",
                    headers=self.headers,
                    params=self.params)
        try:
            return res.json()
            res_json = res.json()["data"]["children"]
            return {"author": res_json[0]["data"]["author"],
                "full": res_json}  # FIXME make selection only!
        except:
            # Problem if banned! Check response headers before checking data!
            print("Exception:", sys.exc_info())
            return 1 #res.json()
        
    def run(self):
        for idx, row in self.df.iterrows():
            print("idx", idx)
            self.results[idx] = self.scrape_post(subreddit=row["subreddit.name"], post_id=row["id"])
            break


class ScrapeUsers(RedditScraping):
    def __init__(self, df, data_path, credentials_path, params=None) -> None:
        super().__init__(df, data_path, credentials_path, params)

    def scrape_user(self, username):
        # FIXME include timing to not exceed rate limits; try to access http header again
        res = requests.get(f"https://oauth.reddit.com/user/{username}/about.json",
                    headers=self.headers,
                    params=self.params)
        return res.json() # FIXME make selection only!

    def run(self):
        for idx, row in self.df.iterrows():
            self.results[idx] = self.scrape_user(username=row["username"])
            break