# psmp_classes.py
#!/usr/bin/python

class Peer_Requester:
    asn = 0
    as_set = ""
    as_name = ""
    traffic_level_inbound = 0
    traffic_level_outbound = 0
    peering_agreement_URL = ""
    peering_policy_URL = ""
    peering_directory_URL = ""
    #Need to make this a list of location?
    location = object()
    def __init__(self, asn, location):
        self.asn = asn
        self.location = location
    def add_as_set(self, as_set):
        self.as_set = as_set      
    def add_location_list(self, locations):
        self.location = location
    def add_as_name(self, as_name):
        self.as_name = as_name
    def add_traffic_level(self, inbound, outbound):
        self.traffic_level_inbound = inbound
        self.traffic_level_outbound = outbound
    def add_peering_policy_URL(self, URL):
        self.peering_policy_URL = URL
    def add_peering_agreement_URL(self, URL):
        self.peering_agreement_URL = URL
    def add_peering_directory_URL(self, URL):
        self.peering_directory_URL = URL        
        
    def __str__(self):
        return ("ASN: " + str(self.asn) + "\n"
        "AS_SET: " + self.as_set + "\n"
        "AS_Name: " + self.as_name + "\n"
        "traffic_level_inbound: " + str(self.traffic_level_inbound) + "\n"
        "traffic_level_outbound: " + str(self.traffic_level_outbound) + "\n"
        "peering_agreement_URL: " + self.peering_agreement_URL + "\n"
        "peering_policy_URL: " + self.peering_policy_URL + "\n"
        "peering_directory_URL: " + self.peering_directory_URL + "\n"
        "location: " + str(self.location) + "\n"
        )

class Peer_Responder:
    def __init__(self):
        pass    
      
       
class Location:
# location_shortname: "AMS-IX"
# location_id_namespace: euro-ix-json
# location_id: 42
# required_location: TRUE
# session:
    location_shortname = ""
    location_id_namespace = ""
    location_id = 0
    required_location = False
    # This should be a list of session objects
    session = object()
    def __init__(self):
        pass

    def __init__(self, location_shortname, location_id_namespace, location_id, required_location, session):
        self.location_shortname = location_shortname
        self.location_id_namespace = location_id_namespace
        self.location_id = location_id
        self.required_location = required_location
        self.session = session
               
        
    def __str__(self):
        return ("location_shortname: " + self.location_shortname + "\n"
        "location_id_namespace: " + self.location_id_namespace + "\n"
        "location_id: " + str(self.location_id) + "\n"
        "required_location: " + str(self.required_location) + "\n"
        "session(s): " + str(self.session)
        )
    def __repr__(self):
        return self.__str__()
        
class Session_IPv4:
#ipv4_address: "198.51.100.64/24"
#ipv4_prefix_count: 100
#ipv4_required: TRUE
    ipv4_address = ""
    ipv4_prefix_count = 0
    ipv4_md5 = ""
    ipv4_required = False
    interface_speed = ""
     
    def __init__(self, address, prefix_count, required, ipv4_md5="", interface_speed=""): 
        self.ipv4_address = address
        self.ipv4_prefix_count = prefix_count
        self.ipv4_md5 = ipv4_md5
        self.ipv4_required = required
        self.interface_speed = interface_speed
    def __str__(self):
        return ("IPv4_Address: " + self.ipv4_address + "\n"
        "IPv4_Prefix_Count: " + str(self.ipv4_prefix_count) + "\n"
        "IPv4_MD5: " + str(self.ipv4_md5) + "\n"
        "IP4_required: " + str(self.ipv4_required))
    def __repr__(self):
        return self.__str__()
        
class Session_IPv6:
#ipv6_address: "2001:db8:6544:4::64/64"
#ipv6_prefix_count: 15
#ipv6_required: FALSE  
    ipv6_address = ""
    ipv6_prefix_count = 0
    ipv6_md5 = ""
    ipv6_required = False 
    interface_speed = ""    
   
    def __init__(self, address, prefix_count, required, ipv6_md5="", interface_speed=""): 
        self.ipv6_address = address
        self.ipv6_prefix_count = prefix_count
        self.ipv6_md5 = ipv6_md5
        self.ipv6_required = required
        
    def __str__(self):
        return ("IPv6_Address: " + self.ipv6_address + "\n"
        "IPv6_Prefix_Count: " + str(self.ipv6_prefix_count) + "\n"
        "IPv6_MD5: " + str(self.ipv6_md5) + "\n"
        "IPv6_Required: " + str(self.ipv6_required))
    def __repr__(self):
        return self.__str__()
      
class Person:
# type: technical
# name: Paul Kowalski
# email: pk@peerB.net
# phone: 1-332-555-3453
# 
# type: policy
# name: Jim Smith
# email: js@peerB.net
# phone: 1-332-555-3496
# 
# type: noc
# name: NOC
# email: noc@peerB.net
# phone: 1-332-555-3464
    type = ""
    name = ""
    email = ""
    phone = ""
    def __init__(self):
        pass
    def __init__(self, type, name, email, phone):
        self.type =  type 
        self.name =  name 
        self.email = email
        self.phone = phone
        
    def __str__(self):
        return ("Type: " + self.type + "\n"
        "Name: " + self.name + "\n"
        "Email: " + self.email + "\n"
        "Phone: " + self.phone)
 