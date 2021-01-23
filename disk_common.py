import os
import os.path
from unidecode import unidecode

def ensure_dirs(dpath):
	"""
	If the directory path does not exist,
	then create it!
	"""
	try:
 		os.makedirs(dpath)
	except WindowsError:
		pass

def write_file(filename, data, pdf=False):
        if not pdf:
            with open(filename, 'w') as output:
                output.writelines(unidecode(data))
        else:
            with open(filename, 'wb') as f:
                for chunk in data.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        #f.flush() commented by recommendation from J.F.Sebastian
