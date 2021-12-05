from flask import Flask
from flask_cors import CORS
from routes.main_blueprint import main_bp
from routes.transactions_blueprint import transactions_bp
from routes.analyse_blueprint import analyse_bp
import os


app = Flask(__name__)
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(transactions_bp, url_prefix='/transactions')
app.register_blueprint(analyse_bp, url_prefix='/analyse')

# enable CORS
CORS(app)

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='127.0.0.1', port=3000, debug=True)
