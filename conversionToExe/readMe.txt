1. Need to install pip install pyinstaller
	pip install pyinstaller

2. Go into the directory where your ‘.py’ file is located. and execute following command where pyinstaller.exe "..\python\scripts\"
   pyinstaller --onefile -w "pythonFiletoConvert"

3. exe file is in [dist] folder. [build] folder and [*.spec] is of no use. 
    You can delete these if you want, it will not affect your ‘.exe’ file. 

4. Open ‘dist’ folder above. Here you will get your ‘.exe’ file.



