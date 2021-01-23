from flask import Flask, jsonify, render_template, request

from utils import count_down, anniversary, zone

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", year=anniversary                                                                                                           )


@app.route("/time")
def lapse():
    tz = request.args.get("tz")
    if tz is None:
        return jsonify(count_down(zone))
    else:
        return jsonify(count_down(tz))


if __name__ == "__main__":
    app.run(debug=True)
