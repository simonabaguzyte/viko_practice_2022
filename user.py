class User:
   def __init__(self, id, username, password, name, surname):
      self.id = id
      self.username = username
      self.password = password
      self.name = name
      self.surname = surname

      self.is_admin = False
      self.is_manager = False
      self.is_resident = False

   def is_login_password_valid(self, password):
      return password == self.password
