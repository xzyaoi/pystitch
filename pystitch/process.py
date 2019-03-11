from pystitch.pystitch import Command, CommandError
from os import path


def automatic(directory='.', image_suffix='.jpg', project_name='project.pto'):
    # Generate Project
    commands = []
    commands.append(
        Command('pto_gen', ['-o', 'project.pto', directory+'/*.' + image_suffix]))
    # Generate Control Points
    commands.append(
        Command('cpfind', ['--multirow', '-o', project_name, project_name]))
    # Pruning Control Points
    commands.append(Command('celeste_standalone', [
                    '-i', project_name, '-o', project_name]))
    # Clean
    commands.append(Command('cpclean', ['-o', project_name, project_name]))
    # Find Vertical Lines
    commands.append(Command('linefind', ['-o', project_name, project_name]))
    # Optimising Positions and Geometry
    commands.append(
        Command('autooptimiser', ['-a', '-l', '-s', '-m', '-o', project_name, project_name]))
    # Optimal Crop and Optimal Size
    commands.append(Command('pano_modify', [
                    '-o', 'project.pto', '--center','--fov=AUTO' ,'--canvas=AUTO', '--ldr-file=JPG', project_name]))
    commands.append(Command('hugin_executor', [
                    '--stitching', '--prefix=pystitch', project_name]))
    for each in commands:
        try:
            each.run()
        except CommandError as e:
            print('[pystitch][' + str(e.status) + ']: ' + str(e.message, 'utf-8'))
            break
        
