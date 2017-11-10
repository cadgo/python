import random
import struct
import socket
#comentario

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
    def __init__(self, dstAddr, PackCount = 1, timeout = 2):
        self.dstAddr = dstAddr
        self.PackCount = PackCount
        self.timeout = timeout
        self.PacketID  = int((id(timeout) * random.random()) % 65535)
        self.Sequencer = 1
        self.ICMPRq = None
    
    def buildHeader(self, ICMPCode, data):
        header = struct.pack('bbHHh', ICMPCode, 0, 0, self.PacketID, 1)
        check = checksum(header + data)
        packet = struct.pack('bbHHh', ICMPCode, 0, socket.htons(check), self.PacketID, self.Sequencer)
        return packet
    
    def SendPacket(self):
        try:
            PacketToSend = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        except socket.errno as e:
            print("Error en socket {} ".format(e))
        

class ICMPEchoRequest(ICMPRquest):
    ICMP_ECHO_REQUEST = 8
    def __init__(self, *args, **kwargs):
        super(ICMPEchoRequest, self).__init__(*args, **kwargs)

    def buildEchoRequest(self, data='A'):
        self.ICMPRq = self.buildHeader(self.ICMP_ECHO_REQUEST, data)
        
    def test(self):
        print(self.dstAddr)
    
    
    
if __name__ == '__main__':
    a = ICMPEchoRequest('192.168.1.100')
    a.test()
    a.buildEchoRequest('A'*42)
        