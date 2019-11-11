from subprocess import Popen, PIPE, STDOUT
import os
import time
import json
import sys

try:
        import fcntl
except ImportError:
        fcntl = None


class open():
    def __init__(self, filename='', flags=[], radare2home=None):
        self._cmd = self._cmd_process
        if radare2home is not None:
            if not os.path.isdir(radare2home):
                raise Exception('`radare2home` passed is invalid, leave it None or put a valid path to r2 folder')
            r2e = os.path.join(radare2home, 'radare2')
        else:
            r2e = 'radare2'
        if os.name == 'nt':
            # avoid errors on Windows when subprocess messes with name
            r2e += '.exe'
        cmd = [r2e, "-q0", filename]
        cmd = cmd[:1] + flags + cmd[1:]
        try:
            self.process = Popen(cmd, shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=0)
        except:
            raise Exception("ERROR: Cannot find radare2 in PATH")
        self.process.stdout.read(1)  # Reads initial \x00
        self.process.stderr.read(1)
        # make it non-blocking to speedup reading
        self.nonblocking = True
        if self.nonblocking:
            fd = self.process.stdout.fileno()
            if not self.__make_non_blocking(fd):
                Exception('ERROR: Cannot make stdout pipe non-blocking')

    @staticmethod
    def __make_non_blocking(fd):
        if fcntl is not None:
            fl = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
            return True

        if os.name != 'nt':
            raise NotImplementedError()

        import msvcrt
        from ctypes import windll, byref
        from ctypes.wintypes import HANDLE, DWORD, BOOL
        try:
            from ctypes import POINTER
        except:
            from ctypes.wintypes import POINTER

        LPDWORD = POINTER(DWORD)
        SetNamedPipeHandleState = windll.kernel32.SetNamedPipeHandleState
        SetNamedPipeHandleState.argtypes = [HANDLE, LPDWORD, LPDWORD, LPDWORD]
        SetNamedPipeHandleState.restype = BOOL

        h = msvcrt.get_osfhandle(fd)

        PIPE_NOWAIT = DWORD(0x00000001)
        res = windll.kernel32.SetNamedPipeHandleState(h, byref(PIPE_NOWAIT), None, None)
        return res != 0

    def _cmd_process(self, cmd):
        cmd = cmd.strip().replace("\n", ";")
        self.process.stdin.write((cmd + '\n').encode('utf8'))
        r = self.process.stdout
        e = self.process.stderr
        self.process.stdin.flush()
        out = b''
        while True:
            if self.nonblocking:
                try:
                    foo = r.read(4096)
                    er = e.read(4096)
                    print(er)
                except:
                    continue
            else:
                foo = r.read(1)
                er = e.read(1)

            if foo:
                if foo.endswith(b'\0'):
                    out += foo[:-1]
                    out += er[:-1]
                    break
                out += er
                out += foo
            else:
                time.sleep(0.001)
        return out.decode('utf-8', errors='ignore')

    # r2 commands
    def cmd(self, cmd, **kwargs):
        """Run an r2 command return string with result
        Args:
            cmd (str): r2 command
        Returns:
            Returns an string with the results of the command

        res = self._cmd(cmd)
        if res is not None:
            return res.strip()
        return None
        """

        res = self._cmd(cmd, **kwargs)
        if res is not None:
            return res
        return None

    def cmdj(self, cmd, **kwargs):
        """Same as cmd() but evaluates JSONs and returns an object
        Args:
            cmdj (str): r2 command
        Returns:
            Returns a JSON object respresenting the parsed JSON
        """
        result = self.cmd(cmd, **kwargs)

        try:
            data = json.loads(result)
        except (ValueError, KeyError, TypeError) as e:
            sys.stderr.write("r2pipe.cmdj.Error: %s\n" % (e))
            data = None
        return data