import sys


def helloworld():
	print('hello, world')
def hellojupiter():
	print('hello jupiter')

def hello():
	if sys.argv[1] =='Jupiter':
		hellojupiter()
	else:
		helloworld()
		


if __name__ == '__main__':
	hello()
