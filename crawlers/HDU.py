import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "HDU"
    oj_url = ""

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        url = r"http://acm.hdu.edu.cn/userstatus.php?user=" + username
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        temp_list = str(soup.table.find_all("table")[2].script).split("p")
        for record in temp_list:
            if record.startswith("("):
                solved_list.add(self.oj_name+record.split(",")[0][1:])
        return list(solved_list)



