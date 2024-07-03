from flask import Blueprint

# 创建蓝图对象
bp = Blueprint('main', __name__)

# 导入各个视图模块
from . import index, task_management
