from flask import Blueprint
import controllers.main_controller as controller

main_bp = Blueprint('main', __name__)


@main_bp.get('/')
def main():
    data = controller.get()
    return data
