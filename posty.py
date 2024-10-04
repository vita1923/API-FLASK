from model.users import User


class Posty: 

  def __init__(self,text:str,author:User):
    self.text=text
    self.author=author