import subprocess
import shlex
import tempfile
import time

class Runner(object):

    def compile(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def clean_up(self):
        raise NotImplementedError



class CRunner(Runner):

    def __init__(self):
        self.compile_command = "gcc {0} -o {1}"
        self.executable_name = "program_c"

    def compile(self, filename):
        self.filename = filename
        cmd = self.compile_command.format(self.filename, self.executable_name)
        subprocess.call(cmd.split())

    def run(self):
        run_command = './{0}'.format(self.executable_name)
        program_output = subprocess.check_output(run_command.split(), shell=False)
        return program_output

    def clean_up(self):
        clean_up_command = "rm {0}".format(self.executable_name)
        subprocess.call(clean_up_command.split())



class PythonRunner(Runner):
    
    def __init__(self):
        pass

    def compile(self, filename):
        # no need to compile python code! ;)
        self.filename = filename

    def run(self):
        run_command = 'python {0}'.format(self.filename)
        program_output = subprocess.check_output(run_command.split())
        return program_output

    def run_test(self, test_input):
        with tempfile.TemporaryFile() as f:
            f.write(test_input)
            f.seek(0)
            run_command = 'python {0}'.format(self.filename)
            start_time = time.time()
            p = subprocess.Popen(run_command.split(), stdin=f, stdout=subprocess.PIPE)
            p.wait()
            program_stdout, program_stderr = p.communicate()
            end_time = time.time()
            time_elapsed = end_time - start_time
        return program_stdout, time_elapsed


    def clean_up(self):
        pass