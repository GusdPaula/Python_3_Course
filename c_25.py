# Context manager with functions - Building and using
# contect managers

from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        print('Opening...')
        file = open(path, mode, encoding='utf8')

        yield file

    except Exception as e:
       print('An error happened: ', e) 

    finally:
        print('Closing...')
        file.close()


with my_open('c_25.txt', 'w') as file:
    file.write('First line\n', 123)
    print('WITH', file)