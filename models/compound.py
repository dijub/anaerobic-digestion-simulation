class Compound:
    def __init__ (self,
                  id: int,
                  name: str,
                  formula: str,
                  cas_number: str,
                  comp_type: str,
                  weight_molar: float,
                  ):
        self.id = id
        self.name = name
        self.comp_type = comp_type
        self.formula = formula
        self.cas_number = cas_number
        self.weight_molar = weight_molar
        
        self.conc_in_flow = 0
        self.flow_molar = 0 
        
    def __str__(self):
        return self.name
        
        
    def print_properties(self):
        name = f'Name: {self.name}'
        formula = f'Formula: {self.formula}'
        weight_molar = f'Weight Molar: {self.weight_molar}'
        conc_in_flow = f'Concentration in Flow: {self.conc_in_flow}'
        flow_molar = f'Flow Molar: {self.flow_molar}'
        
        print(name)
        print(formula)
        print(weight_molar)
        print(conc_in_flow)
        print(flow_molar)    
