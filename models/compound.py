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
        self.mass = 0
        
    def __str__(self):
        return self.name
       
    def calculate_mass(self):
        self.mass = self.flow_molar * self.weight_molar  
        
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


class Mixture(Compound):
    def __init__(self, name, *compounds:Compound):
        super().__init__(id, name, formula='', cas_number='', comp_type='', weight_molar=0)
        self.compounds = compounds 
        self.name = name
        
    def calculate_properties(self):
        self.calc_weight_molar()
        self.calc_flow_molar()
        self.calculate_mass()
        
    def calc_weight_molar(self):
        mols = sum([compound.mass/compound.weight_molar for compound in self.compounds])
        mass = sum([compound.mass for compound in self.compounds])
        self.weight_molar = mass / mols

    def calc_flow_molar(self):
        flow_molar = sum([compound.flow_molar for compound in self.compounds])
        self.flow_molar = flow_molar 
    
    def composition(self):
        for compound in self.compounds:
            print(f'   -{compound.name}: {compound.flow_molar:.2f} kmol')
            
    def print_properties(self):
        name = f'Name: {self.name}'
        weight_molar = f'Weight Molar: {self.weight_molar}'
        flow_molar = f'Flow Molar: {self.flow_molar}'
        
        print(name)
        print(weight_molar)
        print(flow_molar)    
        print("\nComposition:")
        self.composition()