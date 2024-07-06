from flask import render_template, request, redirect, url_for
from . import bp

@bp.route('/customer-services')
def customer_services():
    return render_template('customer_service/customer_service.html')

@bp.route('/entry')
def customer_entry():
    return render_template('customer_service/customer_entry.html')

@bp.route('/list')
def customer_list():
    return render_template('customer_service/customer_list.html')

@bp.route('/customer-interface', methods=['GET', 'POST'])
def customer_interface():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'assigned_tasks':
            return redirect(url_for('main.assigned_tasks', return_path=url_for('main.customer_interface')))
        elif action == 'task_list':
            return redirect(url_for('main.task_list', return_path=url_for('main.customer_interface')))
        elif action == 'task_publish':
            return redirect(url_for('main.task_publish', return_path=url_for('main.customer_interface')))
        elif action == 'personal_info':
            return redirect(url_for('main.personal_info', return_path=url_for('main.customer_interface')))
    return render_template('customer_service/customer_interface.html')

@bp.route('/personal-info', methods=['GET', 'POST'])
def personal_info():
    return_path = request.args.get('return_path', url_for('main.customer_interface'))
    return render_template('customer_service/personal_info.html', return_path=return_path)
