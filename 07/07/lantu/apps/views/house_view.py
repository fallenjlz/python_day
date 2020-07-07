#!/usr/bin/env python

from flask import Blueprint

house_bp = Blueprint('house',__name__,url_prefix='/house')

@house_bp.route('/')
def house_index():
	return 'house'
