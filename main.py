from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS=[
  {
    'id' : '1',
    'title':'Data Analyst',
    'location':'Bengalur , India',
    'salary':'Rs:10,00,000'
  },
  {
    'id' : '2',
    'title':'Data Scientist',
    'location':'Delhi , India',
    
  },
  {
    'id' : '3',
    'title':'Frontend Developer',
    'location':'remote',
    'salary':'Rs:12,00,000'
  },
  {
    'id' : '4',
    'title':'Backend Developer',
    'location':'remote',
    'salary':'$:18,00,000'
  }
]

@app.route("/") 

def hello_world():
    return render_template('home.html',jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)