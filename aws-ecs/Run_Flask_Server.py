from flask import Flask
from flask import render_template
from api.health import health_blueprint
from api.mydata import mydata_blueprint
from db.postgre_db import MyPostgreDb
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)


# swagger settings
swagger_url = '/swagger'
api_url = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "guru-aws-ecs-webserver-python3"
    }
)

# register blueprints
app.register_blueprint(health_blueprint)
app.register_blueprint(mydata_blueprint)
app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)

print(f"calling postgre db connection")
# get db connection string
db_name = os.getenv('POSTGRE_DB_NAME')
db_user = os.getenv('POSTGRE_DB_USER')
db_password = os.getenv('POSTGRE_DB_PASSWORD')
db_host = os.getenv('POSTGRE_DB_HOST')
db_port = os.getenv('POSTGRE_DB_PORT', "5432")

my_db = MyPostgreDb(db_name, db_user, db_password, db_host, db_port)
#Create table in database if not exists
my_db.create_my_custom_table()


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=80)
