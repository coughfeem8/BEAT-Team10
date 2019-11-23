import sys, os, re
# assuming it is running on the source directory.
if len(sys.argv) != 2:
    print('wrong format: expected "<filename>" do NOT include file type.')
elif os.path.isfile('{}.docx'.format(sys.argv[1])):
    os.system('pandoc -f docx -t html {0}.docx -o resources/documentation/{0}.html \
    --extract-media=resources/documentation/{0}'.format(sys.argv[1]))
else:
    print('"{}.docx" not found on the current directory.'.format(sys.argv[1]))
