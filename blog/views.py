# author:Sole_idol
# filename: views.py
# datetime:2020/8/22 9:38

from flask import Blueprint, render_template, redirect, session
from blog.models import BlogText

blogText_bp = Blueprint('blogText', __name__, url_prefix='/blog_text/')
blogText_bp.template_folder = './templates'


@blogText_bp.route('/write_bt/')
def write_bt():
    return render_template('write_bt.html', title='blog编辑', u_name=session.get('u_name'))
