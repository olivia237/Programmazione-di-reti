# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:52:30 2022

@author: Olivia Rannick Nguemo
Matricola 0000935099
"""

""" username: “olivia”
    Password: “olivia” 
"""

''' Traccia 3- Elaborato Programmazione di Reti - UniversitÃ  di Bologna'''

import sys, signal
import http.server
import socketserver
import threading

#permette di gestire il busy waiting
waiting_refresh = threading.Event()

# Legge il numero della porta dalla riga di comando
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8083
  
class ServerHandler(http.server.SimpleHTTPRequestHandler):        
    def do_GET(self):
        # Scrivo sul file AllRequestsGET le richieste dei client     
        with open("AllRequestsGET.txt", "a") as out:
          info = "GET request,\nPath: " + str(self.path) + "\nHeaders:\n" + str(self.headers) + "\n"
          out.write(str(info))
        if self.path == '/refresh':
            resfresh_pages()
            self.path = '/'
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        
# Nota ForkingTCPServer non funziona su Windows come os.fork ()
# La funzione non Ã¨ disponibile su quel sistema operativo. Invece dobbiamo usare il
# ThreadingTCPServer per gestire piÃ¹ richieste

server = socketserver.ThreadingTCPServer(('127.0.0.1',port),ServerHandler)
#header di tutte le pagine
header_html="""
   
<html>
    <head>
        <style>
  h1{
 text-align:center;
}
.button {
border: none;
color: white;
padding: 16px 32px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 16px;
margin: 4px 2px;
transition-duration: 0.4s;
cursor: pointer;
}

.button1 {
background-color: white; 
color: black; 
border: 2px solid #4CAF50;
}

.button1:hover {
background-color: #4CAF50;
color: white;
}

.button2 {
background-color: white; 
color: black; 
border: 2px solid #008CBA;
}

.button2:hover {
background-color: #008CBA;
color: white;
}
.button3 {
background-color: white; 
color: black; 
border: 2px solid #ba002e;
}

.button3:hover {
background-color:#ba002e;
color: white;
}
.button4{
background-color: white; 
color: black; 
border: 2px solid #0f2c36;
}

.button4:hover {
background-color: #0f2c36;
color: white;
}
.button5 {
background-color: white; 
color: black; 
border: 2px solid #ba5400;
}

.button5:hover {
background-color: #ba5400;
color: white;
}
.button6 {
background-color: white; 
color: black; 
border: 2px solid #ba0092;
}

.button6:hover {
background-color:#ba0092;
color: white;
}
.button7 {
background-color: white; 
color: black; 
border: 2px solid #baa700ea;
}

.button7:hover {
background-color:  #baa700ea;
color: white;
}
.button8 {
background-color: white; 
color: black; 
border: 2px solid  #3200ba;
}

.button8:hover {
background-color:   #3200ba;
color: white;
}

            </style>
    </head>
    <body>
        <title>Azienda Viaggi by Olivia</title>

"""
#i bottoni del header
nav_bar="""
 <br>
        <a class="active" href="http://127.0.0.1:{port}">
            <button class="button button1">Home</button>
        </a>
        <a href="https://127.0.0.1:{port}/volo_page.html">
            <button class="button button2">voli</button>
        </a>
        <a href="https://127.0.0.1:{port}/Hotel_page.html">
            <button class="button button3">Alberghi</button>
        </a>
        <a href="https://127.0.0.1:{port}/luoghi_page.html">
            <button class="button button4">Luoghi turistici</button>
        </a>
        <a href="https://127.0.0.1:{port}/meteo_page.html">
            <button class="button button5">meteo</button>
        </a>
        <a href="https://127.0.0.1:{port}/treno_page.html">
            <button class="button button6">orario treni</button>
        </a>
        <a href="https://127.0.0.1:{port}/affito_page.html">
            <button class="button button7">case vacanze</button>
        </a>
        <a href="http://127.0.0.1:{port}/Relazione.pdf" download="Relazione.pdf">
            <button class="button button8">download</button>
        </a> 
    </br>
""".format(port=port)

 #il foother delle pagine
footer_html= """
       
    </body>
</html>
"""

albergo_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/Hotel_page.html" method="post" style="text-align: center;">
        <h1><strong>Alberghi</strong></h1><br>
        <a href="https://www.tripadvisor.it/Hotels-g187800-zff13-Emilia_Romagna-Hotels.html"><h1>Copri</h1></a>
		  <img src='img/hotel.jpg' width="200" height="200">          
          <p v>Scegli l'albergho che ti conviene!</p>
		</form>
		<br>

""".format(port=port)

volo_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/volo_page.html" method="post" style="text-align: center;">
        <h1><strong>Voli</strong></h1><br>
        <a href="https://www.booking.com/region/it/emilia-romagna.it.html"><h1>Copri</h1></a>
		  <img src='img/volo.jpg' width="200" height="200">          
          <p class=h5>Scegli il volo che ti conviene!</p>
		</form>
		<br>

""".format(port=port)

meteo_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/meteo_page.html" method="post" style="text-align: center;">
        <h1><strong>Meteo</strong></h1><br>
		  <img src='img/meteo.jpg' width="200" height="200">          
          <p class=h5>verifica ta temperatura prima di uscise</p>
          <a href="https://www.meteowebcam.eu/meteo/Emilia+Romagna.html"><h1>scopri</h1></a>
		</form>
		<br>

""".format(port=port)


treno_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/treno_page.html" method="post" style="text-align: center;">
        <h1><strong>Orario treni</strong></h1><br>
         <a href="https://www.trenitalia.com/it.html"><h1>scopri</h1></a>
		  <img src='img/treno.jpg' width="200" height="200">          
          <p class=h5>Pianifica il tuo spostamento col treno</p>
		</form>
		<br>

""".format(port=port)

luogo_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/luoghi_page.html" method="post" style="text-align: center;">
        <h1><strong>Luoghi turistici</strong></h1><br>
        <a href="https://travel.thewom.it/italia/emilia-romagna/posti-poco-conosciuti-emilia-romagna.html"><h1>scopri</h1></a>
		  <img src='img/luoghi.jpg' width="200" height="200">          
          <p class=h5>Idee di alcuni luoghi incredibili da visitare assolutamente</p>
		</form>
		<br>

""".format(port=port)


casa_body="""
<br><br>
		<form action="http://127.0.0.1:{port}/affito_page.html" method="post" style="text-align: center;">
        <h1><strong>Case vacanze</strong></h1><br>
        <a href="https://www.booking.com/holiday-homes/region/it/emilia-romagna.it.html"><h1>scopri</h1></a>
		  <img src='img/case-vacanze.jpeg' width="200" height="200">          
          <p class=h5>Alternativa agli alberghi, case per vacanze </p>
		</form>
		<br>

""".format(port=port)



home_body="""
		<form action="http://127.0.0.1:{port}/home" method="post" style="text-align: center;">
        <h1><strong> Benvenuto nell'Agenzia di Viaggio by Olivia nell'Emilia Romagna</strong></h1>
		  <img src='img/viaggiare-in-famiglia.png' width="500" height="300">          
          <p class=h5>L'Agenzia di Viaggio by Olivia ha per obbiettivo di aiutarvi a pianificare 
          i vostri viaggi e  un soggiorno tranquillo con le migliore offerte</p>
		</form>
		<br>

""".format(port=port)

#permette di gestire il busy waiting
def resfresh_pages():
    print("updating all contents")
    create_Hotel_page()
    create_volo_page()
    create_meteo_page()
    create_treno_page()
    create_affito_page()
    create_luoghi_page()
    create_index_page()
    print("finished update")

# creazione della degi alberghi
def create_Hotel_page():
    create_page_servizio("<h1>Hotels</h1>"  , 'Hotel_page.html' ,albergo_body)
# creazione della volo_page
def create_volo_page():
    create_page_servizio("<h1>Voli</h1>"  , 'volo_page.html' ,volo_body)
# creazione pagina meteo
def create_meteo_page():
    create_page_servizio("<h1>Meteo</h1>" , 'meteo_page.html' ,meteo_body)
#creazione pagina treno
def create_treno_page():
    create_page_servizio("<h1>orario treni</h1>"  , 'treno_page.html' , treno_body)
#creazione mappa_page
def create_luoghi_page():
    create_page_servizio("<h1>Luoghi turistici</h1>"  , 'luoghi_page.html' ,luogo_body)
#creazione pagina affito_page
def create_affito_page():
    create_page_servizio("<h1>case Vacanze</h1>"  , 'affito_page.html' ,casa_body)
# creazione della pagina index.html, contiene tutte le altre pagine
def create_index_page():
    create_page_servizio("<h1>Home</h1>", 'index.html' ,home_body)
    
#metodo per la creazione di una generica pagina
def create_page_servizio(title,page_html,page_body):
    f = open(page_html,'w', encoding="utf-8")
    try:
        message = header_html + title + nav_bar + page_body + footer_html
    except:
        pass
    f.write(message)
    f.close()
    




# faccio partire un thread, che ogni 300 secondi aggiorna tutti i contenuti delle pagine
def launch_thread_resfresh():
    t_refresh = threading.Thread(target=resfresh_pages())
    t_refresh.daemon = True
    t_refresh.start()
#definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if(server):
        server.server_close()
    finally:
      waiting_refresh.set()
      sys.exit(0)

# metodo utilizzato all'avvio del server
def main():
    #controllo sulle credenziali di accesso
    username = input("Inserire username: ")
    pw = input("Inserire password: ")
    #se usr o pw sono diverse, chiudo il server e esco
    if (username != 'olivia' or pw != 'olivia') :
        print("Errore durante l'autenticazione dell'utente, riprovare")
        server.server_close()
        sys.exit(0)
    print("Autenticazione avvenuta con successo.\n\n")
        
    launch_thread_resfresh()
    #Assicura che da tastiera usando la combinazione
    #di tasti Ctrl-C termini in modo pulito tutti i thread generati
    server.daemon_threads = True  
    #il Server acconsente al riutilizzo del socket anche se ancora non Ã¨ stato
    #rilasciato quello precedente, andandolo a sovrascrivere
    server.allow_reuse_address = True  
    #interrompe lâesecuzione se da tastiera arriva la sequenza (CTRL + C) 
    signal.signal(signal.SIGINT, signal_handler)
    
    #cancello i dati ogni volta che il server viene aviato
    f = open('AllRequestsGET.txt','w', encoding="utf-8")
    f.close()
    # entra nel loop infinito
    try:
      while True:
        #sys.stdout.flush()
        server.serve_forever()
    except KeyboardInterrupt:
      pass
    server.server_close()

if __name__ == "__main__":
    main()