#!/usr/bin/env python

from flask import Blueprint,render_template
from apps.models.blog_model import Blog

blog_bp = Blueprint('blog',__name__,url_prefix='/blog')

blogs = []

@blog_bp.route('/',endpoint='index')
def blog_index():
	blog = Blog('good time','content','bill')
	blogs.append(blog)
	return render_template('blog/index.html',blogs=blogs)
