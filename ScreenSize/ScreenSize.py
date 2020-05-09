import ctypes

x = ctypes.windll.user32.GetSystemMetrics(0)
y = ctypes.windll.user32.GetSystemMetrics(1)
'''
POC: Detects the screen size and if its under 200 for either x or y then it exits
'''
if x <= 200 or y <= 200:
	print("Possibly running in a vm!")
	exit(0)

print("All is well") 