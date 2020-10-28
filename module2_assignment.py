"""OOP examples for 3_2_assignment"""

import pandas as pd

class Vehicle:
    def __init__(self, color, style, model):
        self.color = str(color)
        self.style = str(style)
        self.model = str(model)
        self.df_vehicle = pd.DataFrame({
            "color": self.color,
            "style": self.style,
            "model": self.model
        },
        index=[0],
        )

    
    def start_selling(self):
        return "(We have a wide range of styles, {}. Would you be interested in a {})".format(self.color, self.style)
   
    def honk(self):
        return "beep beep!"

    
    def __repr__(self):
        return '({},{})'.format(self.color, self.style)
    



# subaru = subaru.Vehicle("black", "suv")