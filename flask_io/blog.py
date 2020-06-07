import functools
from .auth import login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flask_io.db import get_db

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
@login_required
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('index.html')
