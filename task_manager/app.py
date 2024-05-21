from flask import Flask, request, render_template, redirect, url_for
from tasks.task import Task
from tasks.task_manager import TaskManager
from tasks.user import User
from tasks.user_manager import UserManager

app = Flask(__name__)

user_manager = UserManager()
task_manager = TaskManager(user_manager)

# Rota principal para listar usuários e suas tarefas
@app.route('/')
def index():
    users = user_manager.get_all_users()
    return render_template('index.html', users=users)

# Rota para criar usuário
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        name = request.form['name']
        user = User(user_id, name)
        user_manager.add_user(user)
        return redirect(url_for('index'))
    return render_template('create_user.html')

# Rota para criar tarefa
@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        user_id = int(request.form['user_id'])
        user = user_manager.get_user(user_id)
        task = Task(title, description)
        task_manager.add_task(task)
        if user:
            user.add_task(task)
        return redirect(url_for('index'))
    
    users = user_manager.get_all_users()
    return render_template('create_task.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
