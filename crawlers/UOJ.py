import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "UOJ"
    oj_url = "https://uoj.ac/"

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        url = "https://uoj.ac/user/profile/" + str(username)
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        try:
            temp_list = soup.find_all(class_="list-group")[-1].find_all(class_="list-group-item-text")[-1].find_all("a")
        except:
            return []
        for record in temp_list:
            solved_list.add(self.oj_name+str(record.text))
        return list(solved_list)