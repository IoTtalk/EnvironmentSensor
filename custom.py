import DAN

ServerURL='https://DomainName' 
Comm_interval = 15 # unit:second

def profile_init():
    DAN.profile['dm_name']='Model1'
    DAN.profile['d_name']='EnvX' #DAN.get_mac_addr()[-4:]

def odf():  # int only
    return []

def idf():
    return [
       ('AtPressure', int),
       ('Humidity', int),
       ('Temperature', float),
       ('CO2', float),
    ]
