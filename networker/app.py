"""Simple flask app to generate D3 force graphs."""

from flask import Flask, render_template, url_for, Response
import json
import os.path as path

this_dir, _ = path.split(__file__)
app = Flask(__name__, template_folder=path.join(this_dir, "templates"))
app.secret_key = "super_secret_pssst"


def json_file(filename):
    """Add .json to a basename if it has no extension."""
    _, ext = path.splitext(filename)
    if not ext:
        filename += ".json"
    return filename


def validate(filename):
    """Check whether a file is a json file."""
    try:
        with open(json_file(filename), "r") as f:
            doc = json.load(f)
            if "nodes" not in doc or "links" not in doc:
                return False
            good_nodes = all(field in node for field in ["id", "group"]
                             for node in doc["nodes"])
            good_links = all(field in link
                             for field in ["source", "target", "value"]
                             for link in doc["links"])
            return good_nodes and good_links
    except Exception:
        return False


@app.route("/json/<name>")
def get_json(name):
    """Return the JSON representation of the graph."""
    if validate(name):
        with open(json_file(name), "r") as f:
            return Response(f.read(), mimetype="application/json")
    else:
        return render_template("error.html", name=json_file(name))


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
    if validate(name):
        return render_template("force.html",
                               url=url_for("get_json", name=name),
                               name=name)
    else:
        return render_template("error.html", name=json_file(name))
