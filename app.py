# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

#create the app application object
app = Flask(__name__)

app.config["DEBUG"] = True
# use decoratirs to link the function to a url 
@app.route("/")
#define the view using a function, which returns a string
@app.route("/hello")
def hello_world():
    return "Hello, World?!?!?!?!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name) :
	if name.lower()=="michael" :
		return "Hello, {}".format(name) , 200
	else:
		return "Not Found" , 404

if __name__ == "__main__":
    app.run()

#helpppppp
#help2
#hello_WORLD IS GAY
