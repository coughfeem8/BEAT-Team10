import r2pipe

r = r2pipe.open('/home/work/Downloads/beat-master/binaryAnalysis/server.out')
r.cmd('aaa')
imports = r.cmdj("iij")
for i in imports:
    #var = variable.split()
    #if var[var.index("=")] == ":":
    #    var_value = None
    #    var.insert(var.index('='), var_value)
    print(i)