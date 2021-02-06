import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "Codeforces"
    oj_url = "https://codeforces.com/"

    def get_solved_list(self, username:str) -> list:
        solved_list = set()
        url = r"https://codeforces.com/api/user.status?from=1&handle=" + username
        records = json.loads(requests.get(url).content).get("result")
        if records:
            for record in records:
                if record["verdict"] == "OK":
                    solved_list.add(self.oj_name+str(record["problem"]["contestId"])+record["problem"]["index"])
        return list(solved_list)