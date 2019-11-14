from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mbta_helper/", methods=["GET", "POST"])
# def get_stop(place_name):
#     stop, is_accessible =  find_stop_near(place_name)
#     if stop:
#         if is_accessible == 1:
#             return f'{stop} is wheelchair accessible'
#         else:
#             return f'{stop} is not wheelchair accessible'
def get_stop():
    if request.method == "POST":
        place_name = str(request.form["place_name"])
        stop, is_accessible = find_stop_near(place_name)

        if stop:
            return render_template("mbta_results.html", place_name=place_name, stop=stop, is_accessible=is_accessible)
    return render_template("mbta_helper.html")