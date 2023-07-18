from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	features = []
	feature1 = "Here's feature 1 functionality"
	features.append(feature1)
	feature2 = "This is feature 2 functionality"
	features.append(feature2)
	return f"<p>{features}</p>"
