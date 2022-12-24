from user import User

class Admin(User):
   def __init__(self, id, username, password, name, surname):
      super().__init__(id, username, password, name, surname)

      self.is_admin = True


   # def delete_user(self, user):