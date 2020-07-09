#!/usr/bin/env python

from flask import Blueprint,render_template, url_for, redirect, request
from apps.models.blog_model import Blog

blog_bp = Blueprint('blog',__name__,url_prefix='/blog')

blogs = []

@blog_bp.route('/',endpoint='index')
def blog_index():
	blog = Blog('good time','content','bill')
	if blog in blogs:
		pass
	else:
		blogs.append(blog)

	return render_template('blog/index.html',blogs=blogs)

@blog_bp.route('/add',endpoint='add', methods=['GET','POST'])
def blog_add():
	if request.method == 'POST':
		title = request.form.get('title')
		author = request.form.get('author')
		content = request.form.get('content')
		blog = Blog(title,content,author)
		blogs.append(blog)
		return redirect(url_for('blog.index'))
	return render_template('blog/add_blog.html')

@blog_bp.route('/del/<int:id>',endpoint='del')
def blog_del(id):
	value = blogs.pop(id)
	if value:
		return redirect(url_for('blog.index'))
