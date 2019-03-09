import subprocess

REQUIRED_COMMAND = [
    'hugin_executor',
    'pto_gen',
    'cpfind',
    'cpclean',
    'linefind',
    'autooptimiser',
    'pano_modify',
    'convert',
]

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

def executeCommand(command, args):
    query_command = args.insert(0, command)
    try:
        outputs = subprocess.check_output(query_command, stderr=subprocess.STDOUT, stdout=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        out_code = str(e.returncode)
        raise CommandError(out_code, out_bytes)
    finally:
        print('[pystitch]:' + command + ' ' + str(args) + 'executed!')
    