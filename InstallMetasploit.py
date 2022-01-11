import os,time,sys
os.system('clear')
os.system('figlet Lktploit')
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./50)
slowprint("-"*40)
slowprint("install metasploit on termux".center(40))
slowprint("-"*40)

print('''\033[31m[1] Android 7 or more 
\033[32m[2] Android 5 or 6''')
select = input ('Select Your Android version : ')
if select == '1':
    os.system('apt install unstable-repo')
    os.system('apt install Metasploit')
elif select == '2':
    os.system("wget -O metasploit.sh https://raw.githubusercontent.com/remo7777/Termux-Metasploit/master/metasploit-installer.sh")
    os.system('./metasploit.sh')
else:
    print("Error Restart App")
    time.sleep(1)
    os.system("python InstallMetasploit.py")
