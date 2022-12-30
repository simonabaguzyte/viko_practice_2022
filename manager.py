from user import User

class Manager(User):
   def __init__(self, id, username, password, name, surname):
      super().__init__(id, username, password, name, surname)
      
      self.is_manager = True

   def __str__(self):
      return f"{self.name} {self.surname} <{self.username}>"
