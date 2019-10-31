from PyQt5 import QtCore, QtGui

class AThread(QtCore.QThread):
    def __init__(self, rlocal, terminal):
        super(AThread, self).__init__()
        self.rlocal = rlocal
        self.ter = terminal

    def terminal(self, tab, text):
        if text is not "":
            lastText = tab.terminal_output_textEdit.toPlainText()
            tab.terminal_output_textEdit.setText(lastText + text + "\n")
            tab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)

    def run(self):
        while True:
            #self.terminal(self.ter,"Thread")
            print("Thread")
            x = self.rlocal.cmd("dc")
            print(x)
            if "Cannot continue, run ood?" in x:
                break
            self.rlocal.cmd("dso")
            messageAddr = self.rlocal.cmd("dr rsi")  # Memory location to what recv received is in register rsi.

            lookInBuff = "pxj @" + messageAddr  # create command to get contents of memory where recv received a message.

            messageArr = self.rlocal.cmdj(lookInBuff)  # get contents of memory where recv received a message.

            byteStr = ""  # variable that will hold hex values of message

            # Loop over byte array and remove each hex value (ie each letter sent in message)
            for i in range(len(messageArr)):

                # If found 0 byte...then is end of message in memory.
                if messageArr[i] == 0:
                    break
                # building byte string.
                byteStr = byteStr + str(hex(messageArr[i]))[2:] + " "
            #print(byteStr)