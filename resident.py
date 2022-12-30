from user import User

class Resident(User):
   def __init__(self, id, username, password, name, surname, community_id):
      super().__init__(id, username, password, name, surname)

      self.is_resident = True
      self.community_id = community_id

   def __str__(self):
      return f"Resident {self.name} {self.surname} <{self.username}>"
