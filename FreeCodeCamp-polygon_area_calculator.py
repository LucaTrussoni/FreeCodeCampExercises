class Rectangle:
  def __init__(self,width,height):
    # properties starting with __ are private in python (they can be accessed by class 
    # menbers only)
    # variables starting with _ are protected in python (they can be accessed by class
    # members and subclass members)
    # variables starting with no _ are public, so are accessible from outside the class
    self.__width=width
    self.__height=height
  def set_width(self,width):
    self.__width=width
  def set_height(self,height):
    self.__height=height
  # not required but I like it
  def get_width(self):
    return self.__width
  def get_height(self):
    return self.__height
  # Back to the exercise
  def get_area(self):
    return self.__height*self.__width
  def get_perimeter(self):
    return 2*(self.__height+self.__width)
  def get_diagonal(self):
    return (self.__width**2+self.__height**2)**0.5
  def get_picture(self):
    int_w=int(self.__width)
    int_h=int(self.__height)
    picture="Too big for picture."
    if (int_w<=50) and (int_h<=50):
      picture=""
      row=int_w*"*"+"\n"
      for i in range(int_h):
        picture+=row
    return picture
  def get_amount_inside(self,shape):
    cx=int(self.__width/shape.get_width())
    cy=int(self.__height/shape.get_height())
    return cx*cy
  def __str__(self):
    out_string="Rectangle(width="+str(self.__width)+", height="+str(self.__height)+")"
    return out_string

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)
  def set_side(self,side):
    super().set_width(side)
    super().set_height(side) 
  def get_side(self):
    # height and side are equal
    return super().get_height()
  def set_width(self,side):
    self.set_side(side) 
  def set_height(self,side):
    self.set_side(side)
  def __str__(self):
    out_string="Square(side="+str(self.get_side())+")"
    return out_string
  
