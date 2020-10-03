from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# tells our app where the database is located - using sqlite and the database will be named test and should be located in the project folder
app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///test.db'

# initialize the database
db = SQLAlchemy(app) 

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)