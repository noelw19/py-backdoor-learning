# py-backdoor-learning
small program to learn how  backdoor is created and used, also hopefully how to catch a backdoor that may be in use.

So my understanding of a backdoor with the knowledge i have gained after completing this small project is that it is a program that
consists of two main parts  server nd a client, the server being the capture area, where the dataa from the client is sent and saved for further analysis, 
the client connects to this server and sends user specific data to the server when run, this script could be added to another progrm to run in the background such as a game, app.

The ip used is a loopback address, but later on I may test with a couple of virtual machines in virtualbox.

In this ethical example project I have set it up so that when the client script is run the client connects to the server, the OS info and network info is passed to the server and saved to a targetData file.