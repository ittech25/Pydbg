import ctypes
if ctypes.windll.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(), False) != 0:
	print("Debugger Is Present")
	exit()

print('No Debugger Found')