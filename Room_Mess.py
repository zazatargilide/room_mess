

class Laundry:
  def __init__(self, dirtyness, colour, brand_name):
    self.dirtyness = dirtyness
    self.colour = colour
    self.brand_name = brand_name

  def dirtyness_check(self):
    print("Your " + self.colour + self.type + self.dirtyness)
  
  def brand_check(self):
    print(f"Your " + self.colour + self.type + "from " +self.brand_name)

class Shirt(Laundry):
   def __init__(self, dirtyness, colour, brand_name, neck_shape):
    self.type = " coloured shirt is "
    self.neck_shape = neck_shape
    super().__init__(dirtyness, colour, brand_name)

class Pants(Laundry):
  def __init__(self, dirtyness, colour, brand_name, model_shape):
    self.type = " coloured pants are "
    self.model_shape = model_shape
    super().__init__(dirtyness, colour, brand_name)

red_shirt = Shirt("dirty", "red", "bearshka", "round")
blue_jeans = Pants("dirty", "blue", "h&m", "round")
green_shirt = Shirt("dirty", "green", "second hand", "round")

red_shirt.brand_check()
red_shirt.dirtyness_check()