import json, requests
from bs4 import BeautifulSoup
from urllib import parse


class Crawler:
    oj_name = "LibreOJ"
    oj_url = ""

    def get_solved_list(self, username: str) -> list:
        solved_list = set()
        url = "https://api.loj.ac.cn/api/submission/querySubmission"
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            'content-type': 'application/json'
        }
        data = {
            'submitter': username,
            'status': "Accepted",
            'locale': "zh_CN",
            'takeCount': 10
        }
        maxId = -1
        while True:
            if maxId != -1:
                data['maxId'] = maxId
            res = requests.post(url=url, data=json.dumps(data), headers=headers)
            submissions = json.loads(res.content).get("submissions")
            if not submissions or len(submissions) == 0:
                break
            for record in submissions:
                solved_list.add(self.oj_name + str(record['problem']['id']))
            maxId = submissions[-1]['id'] - 1
        return list(solved_list)