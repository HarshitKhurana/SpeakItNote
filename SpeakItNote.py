#!/usr/bin/python

import socket,os,uuid,sys

def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)
    
    unique=uuid.uuid4()
    unique=str(unique)
    name=os.path.expanduser('~')+"/.config/xpad/content-"+unique.split("-")[0]
    print name
    cmnd="xpad --new-from-file="+name
    print cmnd

    data="Xpad client"

    delete=""
    while len(data):
	data=client.recv(4096)
	if "delete" in data:
		delete=True
		print "Delete this : " + str(delete)
	with open(name,"a") as f:
		f.write(str(data))
		print data
	if "bye" in data:
		break
	#Disconnecting client
		client.close()
    
    print "***Opening Sticky note****"
    os.popen(cmnd)
    if str(delete) is "True":
	os.remove(name)
	
    os.system("gnome-terminal -e ' bash -c auto-write-in-xpad.py '")


tcpsock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR ,1)


tcpsock.bind(("" ,1500))
tcpsock.listen(1)


print( "Listening on IP: ")
os.system('ifconfig  | grep -i "inet\ addr"|cut -d":" -f 2|cut -d " " -f 1')
print "\nListening on port 1500"

print "Wating for client to connect " 
data = "Hello from client for xpad"

(client, ( ip , port)) = tcpsock.accept()

#Client will disconnect after inactivity of 60 seconds
client.settimeout(60)

print "Client connected"
print "Socket as - "+ip+":"+`port`
print "Client will be disconnected after 1 minute of inactivity "

set_keepalive_linux(tcpsock)

