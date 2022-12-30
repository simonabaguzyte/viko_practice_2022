class Community:
   def __init__(self, id, street_name, house_no, city):
      self.id = id
      self.street_name = street_name
      self.house_no = house_no
      self.city = city

   def __str__(self):
      return f"{self.street_name} {self.house_no}, {self.city}"