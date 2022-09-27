import sys


def hello():
	if sys.argv[1] == 'mars':
		hellomars()


	if sys.argv[1] == 'jupiter':
		hellojupiter()
	else:
		helloworld()

def hellomars():
	print('hello, mars')

def hellojupiter():
	print('hello jupiter')

def helloworld():
	print('hello world')

if  __name__ == '__main__':
	hello()
