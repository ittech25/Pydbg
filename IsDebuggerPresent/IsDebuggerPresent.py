import ctypes

if ctypes.windll.kernel32.IsDebuggerPresent() != 0:
	print("Debugger Is Present")
	exit()

print('No Debugger Found')