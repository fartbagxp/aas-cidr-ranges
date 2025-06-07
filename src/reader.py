'''
The intent of this class is to provide a simple method to read from a file.

The file may be in a form of json or raw text.
'''


class FileReader():

  def read(self, path=None):
    if path is None:
      print('No path provided.')
      return None

    try:
      with open(path) as f:
        data = f.read()
        return data
    except IOError:
      print(f'Failed to read from {path}')
      return None
