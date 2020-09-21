'''
The intent of this class is to provide a simple method to write to a file.

The file may be in a form of json or raw text.
'''


class CidrWriter():

  def write(self, path=None, data=None):

    if data is None:
      print(f'No data provided for path: {path}')
      return

    try:
      with open(path, "w") as outfile:
        outfile.write(data)
    except IOError:
      print(f'Failed to write to {path}')
