import sys
import os

if len(sys.argv) != 2:
    print('wrong format: expected "<filename>" do NOT include file type.')
elif os.path.isfile('{}.view'.format(sys.argv[1])):
    os.system('python -m PyQt5.uic.pyuic -x {0}.view -o ../{0}.py'.format(sys.argv[1]))
else:
    print('"{}.view" not found on the current directory.'.format(sys.argv[1]))