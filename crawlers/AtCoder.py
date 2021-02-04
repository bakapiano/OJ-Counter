import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "AtCoder"
    oj_url = "http://atcoder.jp/"

    def get_solved_list(self, username: str) -> list:
        # api from https://github.com/kenkoooo/AtCoderProblems
        solved_list = set()
        url = "https://kenkoooo.com/atcoder/atcoder-api/results?user=" + username
        for record in json.loads(requests.get(url).content):
            if record["result"] == "AC":
                solved_list.add(self.oj_name+record["problem_id"])
        return list(solved_list)