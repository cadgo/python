import random
import struct
import socket
import select
import time
from scapy.layers.inet import ICMP

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
    def __init__(self, dstAddr, timeout = 1):
        self.dstAddr = dstAddr
        self.timeout = timeout
        self.PacketID  = int((id(timeout) * random.random()) % 65535)
        self.Sequencer = 1
        self.ICMPRq = None
        self.data = None
    
    def buildHeader(self, ICMPCode, seq, data):
        self.data = data
        header = struct.pack('bbHHh', ICMPCode, 0, 0, self.PacketID, seq)
        check = checksum(header + data)
        packet = struct.pack('bbHHh', ICMPCode, 0, socket.htons(check), self.PacketID, seq)
        #header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id, 1)

        return packet + data
    
    def ReceivePacketTime(self, PingRcv, timesent):
        receive, w, z= select.select([PingRcv], [], [], self.timeout)
        if not receive:
            return 
        data = PingRcv.recv(1024)
        RcvTime = time.time()
        data = data[20:28]
        type, code, checks, id, seq = struct.unpack('bbHHh', data)
        #Garantizamos que sea el mismo paquete
        if self.PacketID == id:
            return RcvTime - timesent
        else:
            return None
    
    def SendPacket(self):
        try:
            PacketToSend = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        except socket.errno as e:
            print("Error en socket {} ".format(e))
        realhost = socket.gethostbyname(self.dstAddr)
        #print("realizando ping a {} a  {} ".format(self.dstAddr, realhost))
        #PacketToSend.sendto(self.ICMPRq, (realhost,1))
        while self.ICMPRq:
            packet = PacketToSend.sendto(self.ICMPRq, (realhost, 1))
            self.ICMPRq = self.ICMPRq[packet:]
        r = self.ReceivePacketTime(PacketToSend, time.time())
        if r == None:
            timercv = "(timeout!!!)"
        else:
            if r < 1:
                timercv = "(1<s)"
            else:
                timercv = "{}".format(round(r,2))
        print("Reply from: {} time={} data={} Bits".format(self.dstAddr, timercv, len(self.data)))
                    

class ICMPEchoRequest(ICMPRquest):
    ICMP_ECHO_REQUEST = 8
    def __init__(self, *args, **kwargs):
        super(ICMPEchoRequest, self).__init__(*args, **kwargs)

    def buildEchoRequest(self, times =1, data='A'*32):
        self.ICMPRq = self.buildHeader(self.ICMP_ECHO_REQUEST,times, data)
        
    def test(self):
        print(self.dstAddr)
        
    def SendICMP(self, times=1):
        print("Realizando ping a {}".format(self.dstAddr))
        for x in range(1,times+1):
            self.buildEchoRequest(x)
            self.SendPacket()
    
if __name__ == '__main__':
    ICMPEchoRequest('www.google.com').SendICMP(3)
    ICMPEchoRequest('192.168.1.254').SendICMP(8)
    ICMPEchoRequest('1.2.1.3').SendICMP(3)
    
        