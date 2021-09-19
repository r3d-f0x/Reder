import random

def get_random_id():
	charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
	id = ''
	for i in range(8):
		id += random.choice(charset)
	return id