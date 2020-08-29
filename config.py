from flask import Flask

from libs.orm import db
from user.views import user_bp
from blog.views import blogText_bp

app = Flask(__name__)

app.secret_key = "!@#%SDFGDSF%$^adf3465dfsdsfg567#@$^_&DG4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sole:000210wibt@localhost:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(blogText_bp)
