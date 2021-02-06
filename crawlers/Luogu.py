import json, requests
from bs4 import BeautifulSoup
from urllib import parse


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
}


class Crawler:
    oj_name = "Luogu"
    oj_url = "https://www.luogu.com.cn/"

    def get_user_uid(self, username:str):
        url = "https://www.luogu.com.cn/api/user/search?keyword=" + username
        res = json.loads(requests.get(url, headers=headers).content)["users"][0]
        if not res:
            return None
        return res["uid"]

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        user_id = self.get_user_uid(username)
        if not user_id:
            return []
        url = "https://www.luogu.com.cn/user/" + str(user_id) + "#practice"
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
        data = json.loads(parse.unquote(str(soup.script).split("(")[2].split('"')[1]))
        for record in data["currentData"]['passedProblems']:
            solved_list.add(self.oj_name+record["pid"])

        return list(solved_list)
