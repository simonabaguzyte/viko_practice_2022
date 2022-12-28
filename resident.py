from user import User

class Resident(User):
   def __init__(self, id, username, password, name, surname):
      super().__init__(self, id, username, password, name, surname)

      self.is_resident = True
      