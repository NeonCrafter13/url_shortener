from flask import Flask, request, jsonify
from flask import templating
from . import helper
from . import db
from .config import Config

app = Flask(__name__)
Config = Config()

@app.route("/")
def index():
    return templating.render_template("index.html")

@app.route("/r/<token>")
def token(token):
    if token == "":
        return "Please enter a token"
    url = db.get_url(token)
    if not url:
        return templating.render_template("error.html")
    return templating.render_template("redirect.html", url=url)

@app.route("/create_url", methods=["POST"])
def create_url():
    request.get_json(force=True)
    json = request.json
    if json["token"] == "":
        token = helper.generate_random(Config.url_length)
    elif json["token"] != None:
        token = json["token"]
    else:
        token = helper.generate_random(Config.url_length)

    url = json["url"]

    if not url:
        return jsonify(
            {"succes": False, "error": "no Url specified"}
        )

    if len(token) > Config.url_length:
        return jsonify(
            {"succes": False, "error": "token too long"}
        )

    info = db.create_short(token, url)
    if type(info) == str:
        return jsonify(
            {"succes": False, "error": info}
        )

    return jsonify(
            {"succes": True, "token": token}
        )

if __name__ == "__main__":
    app.run("127.0.0.1", "5000")
