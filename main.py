from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)

#  
#  $ flask --app hello run
# * Serving Flask app 'hello'
# * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)