from flask import Flask
from blueprints.carts_blueprint import carts_bp
import os


app = Flask(__name__)
app.register_blueprint(carts_bp, url_prefix='/carts')


@app.route('/')
def get():
    return 'main', 200

# app.logger.debug('This is a DEBUG message')
# app.logger.info('This is an INFO message')
# app.logger.warning('This is a WARNING message')
# app.logger.error('This is an ERROR message')


if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='127.0.0.1', port=3000, debug=True)
