from flask import Flask, render_template, url_for, request, redirect
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

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        # try to add the todo to the db session
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the task'
    else:
        # grabbing everything in the Todo database and ordering them all by date_created
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
        


if __name__ == "__main__":
    app.run(debug=True)