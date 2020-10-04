import os

def destination_matcher(current_dir):
	# Test folder
	try:
	    os.mkdir('test')
	except:
	    pass
	finally:
	    return current_dir + '/test'

def file_maker(file, files):
	filename = 'test_' + file + '.py'
	with open(filename, 'w') as fp: 
		for method in files[file]:
			method = method[:-1]
			fp.write('import unittest\nfrom mock import patch\n')
			fp.write('from ' + file + ' import ' + method + '\n\n')
			fp.write('class test_' + file + '(unittest.TestCase):\n\n')
			fp.write('@patch("requests.get")\n')
			fp.write('test_' + method + 'mock_get):\n')
			fp.write('\t' + method + '\n\n')
			fp.write('\t\tself.assertTrue(mock_put.called)\n')
			fp.write('\t\tself.assertEqual(' + method + '), 200)\n')

def test_generator(test_dir, files):
	os.chdir(test_dir)
	print(os.getcwd())

	for file in files:
		try:
			file_maker(file, files)
		except:
			continue

	# path_parent = os.path.dirname(os.getcwd())
	# os.chdir(path_parent)
