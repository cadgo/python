import random
import struct
import socket
import select
import time

def checksum(source_string):
    sum = 0
    countTo = (len(source_string) / 2) * 2
    count = 0
    while count < countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2
        
    if countTo < len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff
    
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    
    answer = answer >> 8 | (answer << 8 & 0xff00)
    
    return answer

class ICMPRquest(object):
    def __init__(self, dstAddr, PackCount = 1, timeout = 1):
        self.dstAddr = dstAddr
        self.PackCount = PackCount
        self.timeout = timeout
        self.PacketID  = int((id(timeout) * random.random()) % 65535)
        self.Sequencer = 1
        self.ICMPRq = None
    
    def buildHeader(self, ICMPCode, data):
        header = struct.pack('bbHHh', ICMPCode, 0, 0, self.PacketID, 1)
        print(data)
        check = checksum(header + data)
        packet = struct.pack('bbHHh', ICMPCode, 0, socket.htons(check), self.PacketID, self.Sequencer)
        #header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id, 1)

        return packet + data
    
    def ReceivePacketTime(self, PingRcv, timesent):
        receive, w, z= select.select([PingRcv], [], [], self.timeout)
        if receive == 0:
            return
        data = PingRcv.recv(1024)
        RcvTime = time.time()
        data = data[20:28]
        type, code, checks, id, seq = struct.unpack('bbHHh', data)
        #Garantizamos que sea el mismo paquete
        if self.PacketID == id:
            print("Recibimos el mismo paqute con ID {}".format(self.PacketID))
            print("Con un tiempo de {}".format(RcvTime - timesent))
            return RcvTime - timesent
        else:
            return 
    
    def SendPacket(self):
        try:
            PacketToSend = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        except socket.errno as e:
            print("Error en socket {} ".format(e))
        realhost = socket.gethostbyname(self.dstAddr)
        print("realizando ping a {} con la ip {} ".format(self.dstAddr, realhost))
        #PacketToSend.sendto(self.ICMPRq, (realhost,1))
        while self.ICMPRq:
            packet = PacketToSend.sendto(self.ICMPRq, (realhost, 1))
            self.ICMPRq = self.ICMPRq[packet:]
        self.ReceivePacketTime(PacketToSend, time.time())
                    

class ICMPEchoRequest(ICMPRquest):
    ICMP_ECHO_REQUEST = 8
    def __init__(self, *args, **kwargs):
        super(ICMPEchoRequest, self).__init__(*args, **kwargs)

    def buildEchoRequest(self, data='A'):
        self.ICMPRq = self.buildHeader(self.ICMP_ECHO_REQUEST, data)
        
    def test(self):
        print(self.dstAddr)
        
    def SendICMP(self):
        self.buildEchoRequest('A'*42)
        self.SendPacket()
    
if __name__ == '__main__':
    ICMPEchoRequest('www.google.com').SendICMP()
    ICMPEchoRequest('8.8.8.8').SendICMP()
    
        