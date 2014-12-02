import unittest

from oj.runner.runners import CRunner, PythonRunner

class TestRunner(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		c_program = r"""
		int main(){
			puts("Hello world!");
			return 0;
		}
		"""
		cls.c_fname = 'tmp/hello.c'
		with open(cls.c_fname, 'w') as f:
			f.write(c_program)

		python_program = r"print 'Sss!'"
		cls.python_fname = 'tmp/hello.py'
		with open(cls.python_fname, 'w') as f:
			f.write(python_program)

	def test_run_c_program(self):
		runner = CRunner()
		runner.compile(self.c_fname)
		output = runner.run()
		runner.clean_up()
		self.assertEquals(output, "Hello world!\n")

	def test_run_python_program(self):
		runner = PythonRunner()
		runner.compile(self.python_fname)
		output = runner.run()
		self.assertEquals(output, "Sss!\n")

	@classmethod
	def tearDownClass(self):
		# remove tmp dir with stuff
		pass
