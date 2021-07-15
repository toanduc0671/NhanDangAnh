import bluetooth

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  
  data = client_sock.recv(1024)
  print(data.decode("utf-8"))
  
  client_sock.close()
  server_sock.close()

while True:
  receiveMessages()
  
