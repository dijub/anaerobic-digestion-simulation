from models import Reaction


class Reactions:
    def __init__(self):
        self.items = []
        self.populate_list()

    def get_value(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                print("Reaction Found")
                return item
        
        print('Reaction Not Found')   
        
    def populate_list(self):
        self.items = [
            Reaction(
                order_reaction= 1,
                conversion_factor= 1.0,
                step_name_reaction= "Hydrolisis",
                is_reverse=False,
            ),
            Reaction(
                order_reaction= 2,
                conversion_factor= 1.0,
                step_name_reaction= 'Hydrolisis',
                is_reverse= False,
            ),
            Reaction(
                order_reaction= 3,
                conversion_factor= 0.54,
                step_name_reaction= 'Hydrolisis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 4,
                conversion_factor= 1,
                step_name_reaction= 'Hydrolisis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 5,
                conversion_factor= 0.33,
                step_name_reaction= 'Acidogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 6,
                conversion_factor= 0.50,
                step_name_reaction= 'Acidogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 7,
                conversion_factor= 1,
                step_name_reaction= 'Hydrolisis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 8,
                conversion_factor= 1,
                step_name_reaction= 'Acidogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 9,
                conversion_factor= 1,
                step_name_reaction= 'Acetogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 10,
                conversion_factor= 1,
                step_name_reaction= 'Acetogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 11,
                conversion_factor= 1,
                step_name_reaction= 'Acidogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 12,
                conversion_factor= 1,
                step_name_reaction= 'Acetogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 13,
                conversion_factor= 1,
                step_name_reaction= 'Hydrolisis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 14,
                conversion_factor= 1,
                step_name_reaction= 'Acetotrophic Methanogenesis',
                is_reverse= False,
            ),                     
            Reaction(
                order_reaction= 15,
                conversion_factor= 1,
                step_name_reaction= 'Hydrogenotrophic Methanogenesis',
                is_reverse= False,
            ),                     
        ]
        
    
