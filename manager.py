from user import User

class Manager(User):
   def __init__(self, id, username, password, name, surname):
      super().__init__(self, id, username, password, name, surname)

      self.is_manager = True