#!/usr/bin/env python

from flask import Blueprint

ent_bp = Blueprint('ent',__name__,url_prefix='/ent')

@ent_bp.route('/')
def ent_index():
	return 'ent'
