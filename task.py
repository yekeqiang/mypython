#!/usr/bin/env python
from celery import Celery
app = Celery('task', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
	return x + y
