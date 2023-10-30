from socket import*
import subprocess
import webbrowser

def abrir_discord():
  try:
    caminho_do_notebook = r"C:\Users\debor\AppData\Local\Discord\app-1.0.9015\Discord.exe"
    subprocess.Popen([caminho_do_notebook])
  except Exception as e:
    print("Ocorreu um erro ao abrir o notebook:", e)

def abrir_netflix():
  try:
    webbrowser.open("https://www.netflix.com/browse")
  except Exception as e:
    print("Ocorreu um erro ao abrir o site no navegador:", e)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('The server is cready ro receive')

while 1:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifiedMessage = int(message.decode())

  if modifiedMessage == 1:
    abrir_discord()
  elif modifiedMessage == 2:
    abrir_netflix()