import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "Vjudge"
    oj_url = ""

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        url = r"https://vjudge.net/user/solveDetail/" + username
        for oj_name, problems in json.loads(requests.get(url).content)["acRecords"].items():
            for problem_name in problems:
                solved_list.add(oj_name + problem_name)
        return list(solved_list)