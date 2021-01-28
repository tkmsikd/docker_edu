import subprocess
import getpass

uname = getpass.getuser()
subprocess.run(["echo", "hello", str(uname)])
