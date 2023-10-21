from models import Compound
from db import Database

class Compounds:
    def __init__(self):
        self.items = []
        self.db = Database('db/db.db')
        self.populate_list()
        
    def populate_list(self):
        compounds = self.db.get_data('compounds')
        for compound in compounds:
            if compound[1].lower() == 'maltopentaose':
                amylose = list(compound)
                amylopectina = list(compound)
                amylose[1] = 'Amylose'
                amylopectina[1] = 'Amylopectina'
                
                amylose = Compound(*amylose)
                amylopectina = Compound(*amylopectina)    
                self.items.append(amylose)
                self.items.append(amylopectina)
                continue
                   
            compound = Compound(*compound)
            self.items.append(compound)

    def get_value(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        
        print(f'Compound "{name}" Not Found')
        
    def print_compound(self):
        for compound in self.items:
            print(f'{compound}: {compound.formula}')
        
        
        
