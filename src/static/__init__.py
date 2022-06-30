from flask import Flask, render_template, redirect, url_for
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False

@app.route("/home")
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)