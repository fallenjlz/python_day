#!/usr/bin/env python

from apps import create_app

app = create_app()

if __name__ == '__main__':
	print(app.url_map)
	app.run(host = '0.0.0.0')


