import json
from flask import *
from crawlers import SUPPORTED_OJ, CRAWLERS


app = Flask(__name__)

app.config['SECRET_KEY'] = "dev"


# support api
@app.route('/api/<string:oj_name>/<string:username>')
def get_solved_list(oj_name, username):
    if oj_name not in SUPPORTED_OJ:
        return json.dumps({
            "error": True,
            "message": "OJ not supported.",
        })

    return json.dumps({
        "error": False,
        "data": json.dumps(CRAWLERS[oj_name]().get_solved_list(username))
    })


@app.route('/api/supported')
def get_supported_oj():
    return json.dumps(SUPPORTED_OJ)


# frontend pages
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/query")
def query():
    return render_template("query.html", SUPPORTED_OJ=SUPPORTED_OJ, CRAWLERS=CRAWLERS)


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


# support frontend api
@app.route("/frontend/save", methods=['POST', 'GET'])
def frontend_save():
    data = []
    if request.method == 'POST':
        print(request.form)
        for name, record in request.get_json():
            if record != "":
                data.append([name, record])
    session['data'] = data
    return json.dumps({"error": False})


@app.route("/frontend/query", methods=['POST', 'GET'])
def frontend_query():
    return json.dumps(session.get("data"))


if __name__ == '__main__':
    app.run()

