import os
name = '植物大战僵尸扩展'
os.system('pyinstaller --workpath builds --distpath builds\distpath --specpath builds\specpath -n '+name+' -w main.py')
