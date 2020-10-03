from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# tells our app where the database is located - using sqlite and the database will be named test and should be located in the project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# initialize the database
db = SQLAlchemy(app) 

# this is similar to the migration files in knex - i am using this class to make the model of the todo
# notice i am giving it an id and then creating the content column as well
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # everytime a todo is created we will return an element with the task id
    def __repr__(self):
        return f"<Task {self.id}>"

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)