from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	features = []
	feature1 = "Here's feature 1 functionality"
	features.append(feature1)
	return f"<p>{features}</p>"
