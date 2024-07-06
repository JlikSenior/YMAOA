from flask import render_template, request, redirect, url_for
from . import bp

@bp.route('/assigned-tasks', methods=['GET', 'POST'])
def assigned_tasks():
    return_path = request.args.get('return_path', url_for('main.index'))
    return render_template('task/assigned_tasks.html', return_path=return_path)

@bp.route('/task-list', methods=['GET', 'POST'])
def task_list():
    return_path = request.args.get('return_path', url_for('main.index'))
    return render_template('task/task_list.html', return_path=return_path)

@bp.route('/task-publish', methods=['GET', 'POST'])
def task_publish():
    return_path = request.args.get('return_path', url_for('main.customer_interface'))
    return render_template('task/task_publish.html', return_path=return_path)
