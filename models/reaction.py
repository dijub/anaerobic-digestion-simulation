from models import Compound 


class Reaction:
    def __init__(self, 
                 order_reaction: int, 
                 conversion_factor: float,
                 step_name_reaction: str,
                 is_reverse: bool,
                 ):
        self.order_reaction = order_reaction
        self.conversion_factor = conversion_factor
        self.step_reaction = step_name_reaction
        self.is_reverse = is_reverse
        self.reagents = []
        self.products = []
        self.flow_inlet = 0
        
    def start(self):
        self.print_reaction()
        self.calc_flow_mol()
        self.calc_reaction_extent()
        self.calc_flow_outlet()
        self.print_result()
    
    def calc_flow_mol(self):
        for _, reagent in self.reagents:
            if not reagent.flow_molar:
                reagent.flow_molar += reagent.conc_in_flow * self.flow_inlet / reagent.weight_molar  
        
        for _, product in self.products:
            if not product.flow_molar:
                product.flow_molar += product.conc_in_flow * self.flow_inlet / product.weight_molar           
        
    def calc_reaction_extent(self):
        reaction_extents = [- reagent.flow_molar / coef for coef, reagent in self.reagents]
        self.reaction_extent = min(reaction_extents) * self.conversion_factor
        
    def calc_flow_outlet(self):
        for coef, reagent in self.reagents:
            reagent.flow_molar = reagent.flow_molar + coef * self.reaction_extent
            reagent.calculate_mass()
        
        for coef, product in self.products:
            product.flow_molar = product.flow_molar + coef * self.reaction_extent       
            product.calculate_mass()    
            
    def print_reaction(self):
        arrow = '-->' if not self.is_reverse else '<-->'
        reagents_side_str = ''
        products_side_str = ''
        
        for coef, reagent in self.reagents:
            if reagents_side_str:
                reagents_side_str += ' + '
            
            formula = reagent.formula
            coef_stoich = coef * -1
            if coef_stoich == 1:
                coef_stoich = ''
                
            reagents_side_str += f'{coef_stoich}{formula}'
            
        for coef, product in self.products:
            if products_side_str:
                products_side_str += ' + ' 
                
            formula = product.formula
            coef_stoich = coef if coef != 1 else ''
            products_side_str += f'{coef_stoich}{formula}'
    
                
        print(f'{reagents_side_str} {arrow} {products_side_str}')
        
        
    def print_result(self):
        for _, compound in  (self.reagents + self.products):
            print(f'{compound.formula:} {compound.flow_molar:.2f}') 
        
    def add_reagent_product(self, compound_dict):
        for type_compound in compound_dict:
            compounds = compound_dict[type_compound]
            if type_compound == 'reagents':
                self.reagents.extend(compounds)
                
            elif type_compound == 'products':
                self.products.extend(compounds)
                
    
        