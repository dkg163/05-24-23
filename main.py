from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'SFO',
    'salary': '100,000'
  },
    {
    'id': 2,
    'title': 'data analyst 2',
    'location': 'SJC',
    'salary': '150,000'
  },
  {
    'id': 3,
    'title': 'data analyst 3',
    'location': 'OAK',
    'salary': '120,000'
  },
]

@app.route("/")
def hello_world():
    return render_template('t1.html', jobs = JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)