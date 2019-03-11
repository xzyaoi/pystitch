from pystitch.process import automatic
from pystitch.pystitch import warmUp

import os
import time

cwd = os.getcwd()

if __name__=='__main__':
    warmUp()
    start = time.time()
    automatic(os.path.join(cwd, 'data2'),'jpg','project.pto')
    end = time.time()
    print('[pystitch]: Finished in :' + str(end-start) + 's')