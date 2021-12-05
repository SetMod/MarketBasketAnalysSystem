from flask import Blueprint
from controllers import analyse_controller

analyse_bp = Blueprint('analyse', __name__)


@analyse_bp.get('/')
def get_analyse():
    res = analyse_controller.get_analyse()
    return res
