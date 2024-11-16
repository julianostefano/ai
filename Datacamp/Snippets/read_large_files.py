# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data
