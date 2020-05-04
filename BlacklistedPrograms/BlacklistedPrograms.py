import psutil  
'''
I would NEVER use psutil but im lazy and Id rather not rewrite the proc checker in ctypes shame me all you want
'''

BLACKLIST = [  
"filemon.exe",
"regmon.exe",
"dbgview.exe",
"diskmon.exe",
"windbg.exe",
"ollydbg.exe",
"procmon.exe",
"immunitydebugger.exe",
"wireshark.exe",
"x32dbg.exe",
"x64dbg.exe",
]
DEBUGGED = False

for p in psutil.process_iter():
    for i in BLACKLIST: 
        if p.name() == i:
            DEBUGGED = True
            break
if DEBUGGED == True:
    print("Sketchy RE program exists")
    exit()
print("Our program is good")