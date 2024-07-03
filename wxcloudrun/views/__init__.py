from flask import Blueprint

bp = Blueprint('main', __name__)

from . import index, task_management
