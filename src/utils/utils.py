import hashlib
import os
import logging
import tqdm
import sys

class TqdmLoggingHandler(logging.Handler):
	def __init__(self, level=logging.NOTSET):
		super().__init__(level)

	def emit(self, record):
		try:
			self.setFormatter(logging.Formatter(("[%(levelname)s\033[0m] "
				"\033[1;31m%(module)s\033[0m: "
				"%(message)s")))
			self.setLevel(record.lvl)
			msg = self.format(record)
			tqdm.tqdm.write(msg)
			self.flush()
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			self.handleError(record)

def setup_logger():
	""" Sets up the logger """
	logging.basicConfig(format=("[%(levelname)s\033[0m] "
		"\033[1;31m%(module)s\033[0m: "
		"%(message)s"),
		level=logging.INFO,
		stream=sys.stdout)
	logging.addLevelName(logging.ERROR, '\033[1;31mE')
	logging.addLevelName(logging.INFO, '\033[1;32mI')
	logging.addLevelName(logging.WARNING, '\033[1;33mW')
	logging.addLevelName(logging.CRITICAL, '\033[1;33mC')

def md5(string):
	"""
	Generates a md5 hash based on the parsed string

	Arguments:
		string (str) -- a string to be encoded
	"""

	hash_md5 = hashlib.md5(str(string).encode())
	return hash_md5.hexdigest()

def md5_file(fname):
	"""
	Generates a md5 hash based on the file parsed

	Arguments:
		fname (str) -- location of the file ('/home/bob/pic.png')
	"""

	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def get_image(image):
	"""
	Get the absolute path of a passed file (image)

	Arguments:
		image (str) -- location of the file
	"""
	if os.path.isfile(image): 
		return os.path.abspath(image)

def get_dir_imgs(img_dir):
	"""
	Get a list of all images in a directory

	Arguments:
		img_dir (str) -- the directory where the images are stored
	"""
	file_types = ("png", "jpg", "jpeg")
	return [img.name for img in os.scandir(img_dir)
			if img.name.lower().endswith(file_types)]