* Harshit Khurana
* hkhurana3@gmail.com
* 25.01.18


SpeakItNote : It is a program that helps to make notes, by speaking into the android application and the sticky notes will be made on the laptop.

-> It works on Client-Server architecture.

-> Sending "bye" to the server will kill the connection, stop writing and open up the sticky note.

-> Sending "delete" to the server will, though open up the stick note at once but will delete it once the sticky note is closed.

-> If the client i.e Android Application does not send any message for 1 minute after starting the connection, it will automatically close the note.

-> To use first start the Python Server on the laptop and then connect to the Laptop/Server using Android Application. 

Tried and Tested using python2.7 and Ubuntu 16.04.3 LTS(Gnome Desktop Environment) and Android Smartphone.

INSTALLATION :

* To install 'xpad' run :

	`sudo apt-get -y install xpad`	
 
* To execute the program :

	`python SpeakItNote.py` : It will start the python server which will accept any incoming connections and make notes of it.


