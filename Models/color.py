class Color:
    def __init__(self, name, red, green, blue, alpha):
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
    
    def __str__(self):
        return "Color: " + self.name + " | red: " + self.red + " | green: " + self.green + " | blue: " + self.blue + " | alpha: " + self.alpha