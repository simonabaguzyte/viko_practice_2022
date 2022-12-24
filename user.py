class User:
   def __init__(self, id, username, password, name, surname):
      self.id = id
      self.username = username
      self.password = password
      self.name = name
      self.surname = surname

      # self.validate_username(username)
      # self.validate_password(password)
      

   def is_login_password_valid(self, password):
      return password == self.password


   # def validate_username(self, username):
   #    if username == None or username.strip() == "":
   #       raise ValueError("First name must not be null or whitespace")

   # def validate_password(self, password):
   #    if password == None or password.strip() == "":
   #       raise ValueError("Last name must not be null or whitespace")



#from user.py program
# from person import Person

# class Administrator(Person):
#    def __init__(self, first_name, last_name, username, password):
#       super().__init__(first_name, last_name)

#       self.username = username
#       self.password = password

#    def update_password(self, old_password, new_password):
#       if self.password == old_password:
#          self.password = new_password
#       else:
#          raise ValueError("Old password does not match the current password")

#    def __str__(self):
#       return f'{self.username}'



