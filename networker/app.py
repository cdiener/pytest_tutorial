"""Simple flask app to generate D3 force graphs."""

from flask import Flask, render_template, url_for, Response
import json
import os.path as path

app = Flask(__name__)
app.secret_key = "super_secret_pssst"


def json_file(filename):
    """Add .json to a basename if it has no extension."""
    _, ext = path.splitext(filename)
    if not ext:
        filename += ".json"
    return filename


def validate(filename):
    """Check whether a file is a json file."""
    with open(json_file(filename), "r") as f:
        try:
            json.load(f)
            return True
        except Exception:
            return False


@app.route("/json/<name>")
def get_json(name):
    """Return the JSON representation of the graph."""
    with open(json_file(name), "r") as f:
        return Response(f.read(), mimetype="application/json")


@app.route("/validate/<name>")
def get_validation(name):
    """Return the JSON representation of the graph."""
    if validate(name):
        result = "Yup, a valid JSON file!"
    else:
        result = "Nope, not a valid JSON file!"

    return Response(result, mimetype="text/plain")


@app.route("/<name>")
def force_graph(name):
    """Render the graph."""
    return render_template("force.html",
                           url=url_for("get_json", name=name),
                           name=name)
