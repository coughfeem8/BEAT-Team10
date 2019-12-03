from PyQt5 import QtCore


class DynamicThread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)
    listSignal = QtCore.pyqtSignal(dict)
    stopSignal = QtCore.pyqtSignal()
    errorSignal = QtCore.pyqtSignal(str)

    def __init__(self, rlocal, pois):
        super(DynamicThread, self).__init__()
        self.rlocal = rlocal
        self.pois = pois

    def run(self):
        """
        Creates a breakpoint for each of the passed pois and analyse the returns and parameters
        :return: None
        """
        try:
            for poi in self.pois:
                poi_location = poi["from"]
                r2_breakpoint = 'db ' + poi_location
                self.rlocal.cmd(r2_breakpoint)

                x = self.rlocal.cmd("dc")
                poi["rtnPara"] = self.check_parameters()
                if "Cannot continue, run ood?" in x:
                    break
                self.textSignal.emit('r2 > \n'+x)
                y = self.rlocal.cmd("dso")
                self.textSignal.emit('r2 > \n'+y)

                poi["rtnFnc"] = self.check_return()

                self.listSignal.emit(poi)
        except Exception as e:
            self.errorSignal.emit(str(e))


    def check_return(self):
        """
        Analysis the RSI register and get the return value of the function
        :return: String Value of return fucntion
        """
        message_addr = self.rlocal.cmd("dr rsi")
        look_in_buff = "pxj @" + message_addr
        message_arr = self.rlocal.cmdj(look_in_buff)
        byte_str = ""

        for i in range(len(message_arr)):
            if message_arr[i] == 0:
                break
            byte_str = byte_str + str(hex(message_arr[i]))[2:]

        if "ffffffff" not in byte_str:
            poi = byte_str
        else:
            poi = "No Value"
        return poi

    def check_parameters(self):
        """
        Gets the value of the parameters passed to the function
        :return: List of values
        """
        self.rlocal.cmd("s")
        i = 0
        parameter_values = []
        seen = []
        while True:
            i += 1
            code = self.rlocal.cmdj('pdj ' + str(-i))
            if code[0]['type'] == 'mov' or code[0]['type'] == 'lea':
                split_cmd = code[0]['opcode'].replace(',', '').split()
                if len(split_cmd) < 2:
                    pass
                elif not (split_cmd[1] in seen):
                    if split_cmd[1] == 'qword':
                        x = " ".join(split_cmd[2:-1]).replace('[', '').replace(']', '')
                        parameter_value = self.rlocal.cmd('dr ' + x)

                    elif split_cmd[1].__contains__("word"):
                        pass
                    else:
                        x = split_cmd[1]
                        parameter_value = self.rlocal.cmd('dr ' + x)
                        seen.append(split_cmd[1])
                parameter_values.append(parameter_value)
            else:
                break
        return parameter_values

    def input(self, text):
        """
        Pass an input to the Debugging session
        :param text: String input to pass
        :return: None
        """
        self.rlocal.process.stdin.write((text + '\n').encode('utf8'))