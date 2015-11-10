# psmp_validator.py
#!/usr/bin/python
 
import sys
from psmp import psmp_classes

def main():
    #print(sys.argv[1])
    req = psmp_classes.Peer_Requester(12200,'AS-RACK')
    print(req)
    
    peering_location = psmp_classes.Location("AMS-IX", "euro-ix-json", 42, True)
    print(peering_location)
    
    sessions = list()
    sessions.append(psmp_classes.Session_IPv4("192.0.1.1", 10, True))
    sessions.append(psmp_classes.Session_IPv6("2001:1::1", 4, False))
    for s in sessions:
        print(s)
      
    persons = list()
    persons.append(psmp_classes.Person("NOC", "Rack NOC", "noc@peeringB.net", "312.555.1241"))
    persons.append(psmp_classes.Person("Policy", "Paul G", "pg@peeringB.net", "312.555.1242"))
    persons.append(psmp_classes.Person("Technical", "Ted H", "th@peeringB.net", "312.555.1243"))
    
    for p in persons:
        print(p)
        
    
    
    

def test_init():
    req = psmp_classes.Peer_Requester()
    res = psmp_classes.Peer_Responder()
    loc = psmp_classes.Location()
    sess = psmp_classes.Session()
    contacts = psmp_classes.Person()
    #print(type(req),type(res), type(loc), type(sess), type(contacts))
        
if __name__ == '__main__':
    main()
	
