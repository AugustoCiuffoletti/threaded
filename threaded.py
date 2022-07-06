#!/usr/bin/python 
import socket, _thread
def servizio(client):                                 #-- Funzione che incapsula il servizio
    data = client.recv(buflen)                        # Attende il dato dal client
    if data: 
        client.send(data)                             # La rispedisce indietro
    print ('Stringa scambiata: ' + data.decode("utf-8"))
    client.close()                                    # Chiude il socket
                                                      #-- Fine della funzione "servizio"
port = input('Su quale porta apri il servizio?\n> ') 
( queuelen, buflen ) = ( 5, 80 ) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creazione del socket
s.bind(('',int(port)))                                # Collegamento della porta al socket
s.listen(queuelen)                                    # Predisposizione della coda
try:
    while 1:
        (client, (remhost, remport))=s.accept()       # Attesa della richiesta (3-way handshake)
        print ('Servizio attivo con '+remhost)
        _thread.start_new_thread(servizio,(client,))   # Invocazione di un thread di servizio
except KeyboardInterrupt:
    print('\n*** Interruzione!')
