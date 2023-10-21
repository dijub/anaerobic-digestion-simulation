from models import Reactor


composition = {
    'amylopectina': 4.29227,
    'amylose': 1.07307,
    'water': 980.00768,
    'ethanol': 0.4825,
    'acetic acid': 0.46070,
    'protein': 7.9,
    'ammonia': 0.06153,
    'triolein': 2.815,
    'propionic acid': 0.151,
    'butyric acid': 1.89307,
    'lactic acid': 0.86318
    
} # kg/m3
flow = 90 #m3

reactor = Reactor(flow, composition)
reactor.start_reactor()