import psutil  
import os
'''
I would NEVER use psutil but im lazy and Id rather not rewrite the proc checker in ctypes shame me all you want
'''
'''
"cmdvrt32.dll", #comodoSandbox
"SxIn.dll", #qihoo360Sandbox #working on adding dll support
"SbieDll.dll" #sandboxie
'''
INVM = [  
"vboxservice.exe",
"vboxtray.exe",
"vmtoolsd.exe",
"vmwaretray.exe",
"vmwareuser",
"VGAuthService.exe",
"vmacthlp.exe",
"vmsrvc.exe",
"vmusrvc.exe",
"prl_cc.exe",
"prl_tools.exe",
"xenservice.exe",
"qemu-ga.exe"
]# https://github.com/LordNoteworthy/al-khaser Check this dudes stuff out, I took this vm list from there.

SANDBOX = False

for p in psutil.process_iter():
	print(p)
	for i in INVM: 
		if p.name() == i:
			SANDBOX = True
			break

if SANDBOX == True:
    print("Our program is in a sandbox")
    exit()
print("Our program is good")
