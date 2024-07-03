from flask import render_template
from . import bp

@bp.route('/task-management')
def task_management():
    return render_template('task_management/task_management.html')
