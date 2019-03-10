import subprocess

REQUIRED_COMMAND = [
    'hugin_executor',
    'pto_gen',
    'cpfind',
    'cpclean',
    'linefind',
    'autooptimiser',
    'celeste_standalone',
    'pano_modify',
    'convert',
]


def argsToString(args):
    to_string = ''
    for each in args:
        to_string = to_string + ' ' + each
    to_string = to_string.strip()
    return to_string


class Command(object):
    def __init__(self, name, args):
        if name not in REQUIRED_COMMAND:
            raise CommandError(
                '400', 'Command [' + name + '] cannot be recognized!')
        self.name = name
        self.args = args

    def run(self):
        self.args.insert(0, self.name)
        to_be_executed = argsToString(self.args)
        try:
            outputs = subprocess.check_output(
                to_be_executed, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            out_code = str(e.returncode)
            raise CommandError(out_code, out_bytes)
        finally:
            print('[pystitch]: ' + to_be_executed + ' executed!')


class CommandError(RuntimeError):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        self.args = (status, message)


def warmUp():
    for each in REQUIRED_COMMAND:
        try:
            outputs = subprocess.check_output([each], stderr=subprocess.STDOUT)
        except FileNotFoundError as e:
            out_bytes = 'Command ' + each + 'is required but not found in your $PATH'
            out_code = '404'
            raise CommandError(out_code, out_bytes)
        except subprocess.CalledProcessError as e:
            pass
    print('[pystitch]: Test Finished!')

def cleanIntermediateFile():
    print('[pystitch]: Intermediate Files Deleted')