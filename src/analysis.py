import r2pipe


def static_analysis(binary_file):
    try:
        rlocal = r2pipe.open(binary_file)
        rlocal.cmd("aaa")
        # Gets all functions is JSON format
        functions = rlocal.cmdj("aflj")
        # Gets all variables in JSON format
        variables = rlocal.cmd('afvd').split('\n')
        # Gets all structs in JSON format
        all_recvs = rlocal.cmdj("axtj sym.imp.recv")
        all_sends = rlocal.cmdj("axtj sym.imp.send")
        # Gets all strings in JSON format
        strings = rlocal.cmdj("izzj")
        # Gets all imports in JSON format
        imports = rlocal.cmdj("iij")
        return functions, variables, all_recvs, all_sends, strings, imports

    except Exception as e:
        print("Error " + str(e))