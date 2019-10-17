import r2pipe

r = r2pipe.open('/home/work/Downloads/beat-master/binaryAnalysis/server.out')
r.cmd('aaa')
cmd = "doo"
r.cmd(cmd)