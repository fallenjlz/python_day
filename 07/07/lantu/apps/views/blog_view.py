#!/usr/bin/env python

from flask import Blueprint

blog_bp = Blueprint('blog',__name__,url_prefix='/blog')

@blog_bp.route('/')
def blog_index():
	return 'blog'
