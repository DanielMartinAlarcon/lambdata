class Complex:
    def __init__(self, realpart, imagpart):        
        """
        Instantiates the complex number with a real and an imaginary part
        """
        num_type = (int, float)
        
        if isinstance(realpart, num_type) and isinstance(imagpart, num_type):
            self.r = realpart
            self.i = imagpart
        else:
            print("Hey, that's not a number!")
        
    def add(self, real, imag):
        """
        Takes a new complex number and adds it to the one that the class was 
        originally instantiated with.
        """
        new_real = self.r + real
        new_imag = self.i + imag
        
        return Complex(new_real, new_imag)