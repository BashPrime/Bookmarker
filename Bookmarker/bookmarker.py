import socket

# Variables
nick = 'Ziltoid'
debug = True #For debugging purposes
network = 'irc.freenode.net' #Define the IRC network
port = 6667 #Define the IRC server port

if debug == True:
	chan = ''
	chanpass = ''
	
else:
	chan = ''
	chanpass = ''

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define the IRC socket
irc.connect((network,port)) #Connect to the IRC server

irc.recv(4096) #Set up the buffer
irc.send('NICK ' + nick + '\r\n') #Send the bot's current nick
irc.send('USER Ziltoid Ziltoid Ziltoid :Ziltoid IRC\r\n') #Send user info to the server
irc.send('JOIN ' + chan + ' ' + chanpass + '\r\n') #Join the defined channel
irc.send('PRIVMSG ' + chan + ' :Hello!\r\n') #Send a message to the channel

while True:
	data = irc.recv (4096)
	print data #For debugging purposes
	if data.find('PING') != -1:
		irc.send(('PONG') + data.split()[1] + '\r\n')
