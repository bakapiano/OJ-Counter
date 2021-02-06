# OJ-Counter

基于 Python 和 Flask 的轻量级 OnlineJudge 过题数统计网站。

Demo: [oj-counter.bakapiano.site](https://oj-counter.bakapiano.site/)

## 概览

+ 使用 Docker 一键部署
+ 爬虫在服务器端运行，无数据库

## API

返回结果均为 json 格式。

### 查询支持的 OJ

```/api/supported```

返回支持的 OJ 列表。

example: https://oj-counter.bakapiano.site/api/supported

### 查询用户在某个 OJ 上的过题情况

``/api/<oj_name>/<username>``

在 data 段返回用户在该 OJ 上的过题列表，格式为 OJ名+题号，注意 oj_name 需与 ```/api/supported``` 中的 OJ 名称完全一致。

example: https://oj-counter.bakapiano.site/api/Luogu/zzq233

## 部署

## 贡献爬虫代码

**你只需专注于爬虫代码的编写，在文件创建后其他部分（前端后端）都会被自动配置好。

爬虫代码在项目 /crawlers 目录中，命名格式为 ```OJ名称.py```，爬虫编写格式如下：

```python
import json, requests #请将用到的额外库加入到 requirement.txt 中

class Crawler: #类名固定为 Crawler
    oj_name = "AtCoder" #OJ名称，请保持与文件名一致。
    oj_url = "http://atcoder.jp/" #OJ地址

    def get_solved_list(self, username: str) -> list:
        # 编写你的爬虫代码
        # 传入参数为 str 类型的 username，表示待查询用户名
        # 返回一个包含 str 的 list，格式为 OJ名称+题号，表示查询结果

        # api from https://github.com/kenkoooo/AtCoderProblems
        solved_list = set()
        url = "https://kenkoooo.com/atcoder/atcoder-api/results?user=" + username
        for record in json.loads(requests.get(url).content):
            if record["result"] == "AC":
                solved_list.add(self.oj_name+record["problem_id"])

        return list(solved_list)
```
