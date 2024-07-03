from flask import render_template
from . import bp

@bp.route('/task-management')
def task_management():
    return render_template('task_management/task_management.html')

@bp.route('/create-task')
def create_task():
    return render_template('task_management/create_task.html')

@bp.route('/task-list')
def task_list():
    return render_template('task_management/task_list.html')
