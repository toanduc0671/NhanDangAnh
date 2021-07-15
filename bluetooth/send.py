import bluetooth
import time
import subprocess as sp

def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("thong tin broker")
  sock.close()
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices:
    return bdaddr
    
while True
  devices = lookUpNearbyBluetoothDevices()
  for device in devices:
    sendMessageTo(device)
    time.sleep(1)
    sp.call(["rfkill", "block", "bluetooth"])
    time.sleep(2.5)
    sp.call(["rfkill", "unblock", "bluetooth"])