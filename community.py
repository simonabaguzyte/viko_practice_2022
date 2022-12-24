from db import conn
from service import Service

class Community:
   def __init__(self, id, street_name, house_no, city):
      self.id = id
      self.street_name = street_name
      self.house_no = house_no
      self.city = city
      self.services = self._fetch_services()

   def __str__(self):
      return f"{self.street_name} {self.house_no}, {self.city}"

   def _fetch_services(self):
      cursor = conn.cursor()
      sql = f"""
      SELECT s.* FROM services s
      JOIN community_services cs ON cs.service_id = s.id
      WHERE cs.community_id = {self.id}
      """
      cursor.execute(sql)
      services_data = cursor.fetchall()
      cursor.close()
      
      services = []
      for service_data in services_data:
         id = service_data[0]
         name = service_data[1]
         service = Service(id, name)
         services.append(service)

      return services
