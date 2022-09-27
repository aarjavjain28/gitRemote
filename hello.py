import sys

def hello():
	if sys.argv[1] == 'mars':
		hellomars()
	else:
		helloworld()

def hellomars():
	print('hello, mars')

def helloworld():
	print('hello, world')
if __name__ == '__main__':
	hello()
