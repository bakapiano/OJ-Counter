import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "POJ"
    oj_url = "http://poj.org/"

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        url = r"http://poj.org/userstatus?user_id=" + username
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        temp_list = str(soup.find_all("table")[-1].find_all("tr")[2].find_all("td")[-1].script).split("\n")
        for record in temp_list:
            if record.startswith("p("):
                solved_list.add(self.oj_name+record[2:-1])
        return list(solved_list)
