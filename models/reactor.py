from models import Compound
from repositories import Compounds, Reactions

class Reactor:
    def __init__(self, flow: float, composition: dict[str, float]):
        self.flow = flow 
        self.composition = composition
        self.compounds = Compounds()
        
    def start_reactor(self):
        self.set_concentration()
        self.load_reactions()

        print('Starting Reactor..\n')
        for reaction in self.reactions.items:
            print(f'Reaction {reaction.order_reaction}')
            reaction.start()
            print()

    
    def set_concentration(self):
        for item in self.composition:
            compound = self.compounds.get_value(item)
            conc_in_flow = self.composition[item]
            compound.conc_in_flow = conc_in_flow
                        
    
    def load_reactions(self):
        self.reactions = Reactions()
        
        water = self.compounds.get_value('water')
        glucose = self.compounds.get_value('glucose')
        amylopectina = self.compounds.get_value('amylopectina')
        amylose = self.compounds.get_value('amylose')
        protein = self.compounds.get_value('protein')
        methane = self.compounds.get_value('methane')
        carbon_dioxide = self.compounds.get_value('carbon dioxide')
        ammonia = self.compounds.get_value('ammonia')
        hydrogen_sulfide = self.compounds.get_value('hydrogen sulfide')
        triolein = self.compounds.get_value('triolein')
        glycerol = self.compounds.get_value('glycerol')
        oleic_acid = self.compounds.get_value('oleic acid')
        microorganism = self.compounds.get_value('microorganism')
        acetic_acid = self.compounds.get_value('acetic acid')
        propionic_acid = self.compounds.get_value('propionic acid')
        butyric_acid = self.compounds.get_value('butyric acid')
        lactic_acid = self.compounds.get_value('lactic acid')
        hydrogen = self.compounds.get_value('hydrogen')
        ethanol = self.compounds.get_value('ethanol')
        
        reactions_settings = {
            1: {
                'reagents': [(-4, water), (-1, amylopectina)],
                'products': [(5, glucose)]
            },
            2: {
                'reagents': [(-4, water), (-1, amylose)],
                'products': [(5, glucose)]
            },
            3: {
                'reagents': [(-1, protein), (-6, water)],
                'products': [(6.5, methane), (6.5, carbon_dioxide), (3, ammonia), (1, hydrogen_sulfide)]
            },
            4: {
                'reagents': [(-3, water), (-1, triolein)],
                'products': [(1, glycerol), (3, oleic_acid)]
            },
            5: {
                'reagents': [(-1, glucose), (-0.1115, ammonia)],
                'products': [(0.1115, microorganism), (0.744, acetic_acid), (0.5, propionic_acid), (0.4409, butyric_acid), (0.6909, carbon_dioxide), (1.0254, water)]
            },
            6: {
                'reagents': [(-1, glucose)],
                'products': [(2, lactic_acid)]
            },
            7: {
                'reagents': [(-1, glucose)],
                'products': [(2, ethanol), (2, carbon_dioxide)]
            },
            8: {
                'reagents': [(-3, lactic_acid)],
                'products': [(2, propionic_acid), (1, acetic_acid), (1, carbon_dioxide), (1, water)]
            },
            9: {
                'reagents': [(-15.2396, water), (-1, oleic_acid), (-0.1701, ammonia), (-0.2501, carbon_dioxide)],
                'products': [(0.17010, microorganism), (8.6998, acetic_acid), (14.4978, hydrogen)]
            },
            10: {
                'reagents': [(-0.8038, water), (-0.0653, ammonia), (-1, butyric_acid), (-0.0006, hydrogen), (-0.5543, carbon_dioxide)],
                'products': [(0.0653, microorganism), (1.8909, acetic_acid), (0.446, methane)]
            },
            11: {
                'reagents': [(-1, glycerol), (-0.04071, ammonia), (-0.0291, carbon_dioxide), (-0.0005, hydrogen)],
                'products': [(0.04071, microorganism), (0.94185, propionic_acid), (1.09308, water)]
            },
            12: {
                'reagents': [(-0.31434, water), (-1, propionic_acid), (-0.06198, ammonia)],
                'products': [(0.06198, microorganism), (0.9345, acetic_acid), (0.66041, methane), (0.16069, carbon_dioxide), (0.00055, hydrogen)]
            },
            13: {
                'reagents': [(-2, ethanol), (-1, carbon_dioxide)],
                'products': [(2, acetic_acid), (1, methane)]
            },
            14: {
                'reagents': [(-0.022, ammonia), (-1, acetic_acid)],
                'products': [(0.022, microorganism), (0.945, methane), (0.945, carbon_dioxide), (0.066, water)]
            },
            15: {
                'reagents': [(-14.4976, hydrogen), (-3.8334, carbon_dioxide), (-0.0836, ammonia)],
                'products': [(0.08360, microorganism), (3.4154, methane), (7.4996, water)]
            }
        }

        for reaction in self.reactions.items:
            reaction.flow_inlet = self.flow
            order_reaction = reaction.order_reaction
            reagents_products_dict = reactions_settings[order_reaction]
            reaction.add_reagent_product(reagents_products_dict)

        
        
    
    