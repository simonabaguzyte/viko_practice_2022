import PySimpleGUI as sg

from admin import Admin
from community import Community
from db import conn
from manager import Manager
from resident import Resident
from service import Service

# ===========================
# LOGIN
# ===========================

def open_login_window():
   layout = [
      [sg.Text("Welcome to the system of providing communal services to residents!")],
      [sg.Text("Username"), sg.InputText(key="username")],
      [sg.Text("Password"), sg.InputText(key="password", password_char="*")],
      [sg.Button("Sign in"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 1", layout=layout)

# ===========================
# ADMIN
# ===========================

def open_admin_home_window():
   layout = [
      [sg.Text("Manage chosen section:")],
      [
         sg.Button("Communities"),
         sg.Button("Services"),
         sg.Button("Managers"),
         sg.Button("Log out")
      ]
   ]
   return sg.Window(title="PORTAL 2", layout=layout)

# ===========================
# MANAGERS
# ===========================

def open_manager_home_window():
   layout = [
      [sg.Text("Manage chosen section:")],
      [  
         sg.Button("Communities"),
         sg.Button("Log out")
      ]
   ]
   return sg.Window(title="PORTAL 14", size=(300, 100), layout=layout)

def open_admin_manager_window(managers):
   layout = [
      [sg.Text("A list containing all managers:")],
      [
         sg.Listbox(values=managers,
         size=(30, len(managers)),
         key="managers")
      ],
      [sg.Button("Add manager"), sg.Button("Delete manager"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 12", layout=layout)

def open_create_manager_window():
   layout = [
      [sg.Text("First name"), sg.InputText(key="first_name")],
      [sg.Text("Last name"), sg.InputText(key="last_name")],
      [sg.Text("ATTENTION! First name is automatically assigned to be the login name")],
      [sg.Text("and last name to be the password.")],
      [sg.Button("Create manager"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 13", layout=layout)

# ===========================
# COMMUNITIES
# ===========================

def open_admin_communities_window(communities):
   layout = [
      [sg.Text("Manage community of a particular house:")],
      [sg.Listbox(values=communities, size=(30, len(communities)), key="communities")],
      [  
         sg.Button("Add community"),
         sg.Button("Delete community"),
         sg.Button("Assign service"),
         sg.Button("Assign resident"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 3", layout=layout)

def open_manager_communities_window(communities):
   layout = [
      [sg.Text("Manage community")],
      [sg.Listbox(values=communities, size=(30, len(communities)), key="communities")],
      [
         sg.Button("Manage services"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 15", layout=layout)

def open_resident_community_window(community):
   layout = [
      [sg.Text("Community")],
      [sg.Listbox(values=[community], size=(30, 1), key="communities")],
      [
         sg.Button("View services"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 19", layout=layout)

def open_add_community_window():
   layout = [
      [sg.Text("Street name"), sg.InputText(key="street_name")],
      [sg.Text("House number"), sg.InputText(key="house_no")],
      [sg.Text("City"), sg.InputText(key="city")],
      [sg.Button("Create community"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 4", layout=layout)
   
def open_add_service_to_community_window(services):
   layout = [
      [sg.Text("List of services for chosen community:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="services")],
      [  
         sg.Button("Link service"),
         sg.Button("Unlink service"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 5", layout=layout)

def open_not_linked_services_window(services):
   layout = [
      [sg.Text("List of services not yet linked to community:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="services")],
      [
         sg.Button("Link service to community"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 6", layout=layout)

def open_assign_resident_to_community_window(residents):
   layout = [
      [sg.Text("Resident(s) of a chosen community:")],
      [sg.Listbox(values=residents, size=(30, len(residents)), key="residents")],
      [
         sg.Button("Add resident"),
         sg.Button("Delete resident"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 7", layout=layout)

# ===========================
# SERVICES
# ===========================

def open_services_window(services):
   layout = [
      [sg.Text("Choose a service to proceed:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="services")],
      [
         sg.Button("Add service"),
         sg.Button("Delete service"),
         sg.Button("Assign service manager"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 9", layout=layout)

def open_add_service_window():
   layout = [
      [sg.Text("Service name"), sg.InputText(key="service_name")],
      [sg.Button("Create service"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 10", layout=layout)

def open_assign_service_manager_window(managers):
   layout = [
      [sg.Text("Choose a manager to proceed:")],
      [sg.Listbox(values=managers, size=(30, len(managers)), key="managers")],
      [sg.Button("Assign manager"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 11", layout=layout)

def open_manager_services_window(services):
   layout = [
      [sg.Text("Services")],
      [sg.Listbox(values=services, size=(30, len(services)), key="services")],
      [
         sg.Button("Assign service price"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 16", layout=layout)

def open_manager_service_price_window():
   layout = [
      [sg.Text("Charge price for a chosen community's service:")],
      [sg.Text("Price"), sg.InputText(key="price")],
      [sg.Button("Change service price"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 17", layout=layout)

def open_resident_services_window(services):
   layout = [
      [sg.Text("Services")],
      [sg.Listbox(values=services, size=(30, len(services)), key="services")],
      [
         sg.Button("Check service price"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 20", layout=layout)

# ===========================
# RESIDENTS
# ===========================

def open_resident_home_window():
   layout = [
      [sg.Text("Choose:")],
      [sg.Button("Communities"), sg.Button("Log out")]
   ]
   return sg.Window(title="PORTAL 18", size=(300, 100), layout=layout)

def open_create_resident_window():
   layout = [
      [sg.Text("First name"), sg.InputText(key="first_name")],
      [sg.Text("Last name"), sg.InputText(key="last_name")],
      [sg.Text("ATTENTION! First name is automatically assigned to be the login name")],
      [sg.Text("and last name to be the password.")],
      [sg.Button("Create resident"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 8", layout=layout)

# ===========================
# DB OPERATIONS
# ===========================
# ===========================
# COMMUNITIES
# ===========================

def get_communities():
   cur = conn.cursor()
   cur.execute("SELECT * FROM communities")
   communities_data = cur.fetchall()
   cur.close()
   
   communities = list()
   for entry in communities_data:
      id = entry[0]
      street_name = entry[1]
      house_no = entry[2]
      city = entry[3]

      community = Community(id, street_name, house_no, city)
      communities.append(community)

   return communities

def create_community(street_name, house_no, city):
   cursor = conn.cursor()
   sql = f"""
      INSERT INTO communities (street_name, house_no, city)
      VALUES ('{street_name}', '{house_no}', '{city}');
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

def delete_community(community):
   cur = conn.cursor()
   cur.execute(f"DELETE FROM communities WHERE id = {community.id}")
   conn.commit()
   cur.close()

def get_residents_community(resident):
   if resident.community_id is None:
      return None

   cursor = conn.cursor()
   sql = f"""
      SELECT *
      FROM communities
      WHERE id = {resident.community_id}
   """
   cursor.execute(sql)
   community_data = cursor.fetchone()
   cursor.close()
   
   id = community_data[0]
   street_name = community_data[1]
   house_no = community_data[2]
   city = community_data[3]
   community = Community(id, street_name, house_no, city)

   return community

def get_not_linked_services(community):
   cursor = conn.cursor()
   sql = f"""
      SELECT *
      FROM services
      WHERE id NOT IN (
         SELECT service_id
         FROM community_services 
         WHERE community_id = {community.id}
      )
   """
   cursor.execute(sql)
   services_data = cursor.fetchall()
   cursor.close()

   services = list()
   for entry in services_data:
      id = entry[0]
      name = entry[1]

      service = Service(id, name)
      services.append(service)

   return services

def link_service_to_community(community, service):
   cursor = conn.cursor()
   sql = f"""
      INSERT INTO community_services (community_id, service_id)
      VALUES ({community.id}, {service.id})
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

def unlink_service_from_community(community, service):
   cursor = conn.cursor()
   sql = f"""
      DELETE FROM community_services
      WHERE community_id = {community.id}
      AND service_id = {service.id}
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

def get_community_residents(community):
   cursor = conn.cursor()
   sql = f"""
      SELECT *
      FROM users
      WHERE community_id = {community.id}
      AND is_admin = FALSE
      AND is_manager = FALSE
   """
   cursor.execute(sql)
   residents_data = cursor.fetchall()
   cursor.close()

   residents = list()
   for entry in residents_data:
      id = entry[0]
      username = entry[1]
      password = entry[2]
      name = entry[3]
      surname = entry[4]
      community_id = entry[7]

      resident = Resident(id, username, password, name, surname, community_id)
      residents.append(resident)
   
   return residents

# ===========================
# SERVICES
# ===========================

def get_services():
   cur = conn.cursor()
   cur.execute("SELECT * FROM services")
   services_data = cur.fetchall()
   cur.close()

   services = list()
   for entry in services_data:
      id = entry[0]
      name = entry[1]
      service = Service(id, name)
      services.append(service)

   return services

def create_service(name):
   cur = conn.cursor()
   sql = f"INSERT INTO services (name) VALUES ('{name}');"
   cur.execute(sql)
   conn.commit()
   cur.close()

def delete_service(service):
   cur = conn.cursor()
   cur.execute(f"DELETE FROM services WHERE id = {service.id}")
   conn.commit()
   cur.close()

def assign_manager_to_service(service, manager):
   cursor = conn.cursor()
   sql = f"""
      UPDATE services
      SET manager_id = {manager.id}
      WHERE id = '{service.id}'
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

def get_community_services(community):
   cursor = conn.cursor()
   sql = f"""
      SELECT s.*
      FROM services s
      JOIN community_services cs ON cs.service_id = s.id
      WHERE cs.community_id = {community.id}
   """
   cursor.execute(sql)
   services_data = cursor.fetchall()
   cursor.close()

   services = list()
   for entry in services_data:
      id = entry[0]
      name = entry[1]
      service = Service(id, name)
      services.append(service)

   return services

def get_manager_services_for_community(community, manager):
   cursor = conn.cursor()
   sql = f"""
      SELECT s.*
      FROM services s
      JOIN community_services cs ON cs.service_id = s.id
      WHERE cs.community_id = {community.id}
      AND s.manager_id = {manager.id}
   """
   cursor.execute(sql)
   services_data = cursor.fetchall()
   cursor.close()

   services = list()
   for entry in services_data:
      id = entry[0]
      name = entry[1]
      service = Service(id, name)
      services.append(service)

   return services

def change_community_service_price(community, service, price):
   cursor = conn.cursor()
   sql = f"""
      UPDATE community_services
      SET price = {price}
      WHERE community_id = '{community.id}'
      AND service_id = '{service.id}';
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

def get_community_service_price(community, service):
   cursor = conn.cursor()
   sql = f"""
      SELECT price
      FROM community_services
      WHERE community_id = '{community.id}'
      AND service_id = '{service.id}';
   """
   cursor.execute(sql)
   data = cursor.fetchone()
   cursor.close()
   price = data[0]
   return price

# ===========================
# MANAGERS
# ===========================

def get_managers():
   cursor = conn.cursor()
   sql = "SELECT * FROM users WHERE is_manager = TRUE"
   cursor.execute(sql)
   managers_data = cursor.fetchall()
   cursor.close()
   
   managers = list()
   for entry in managers_data:
      id = entry[0]
      username = entry[1]
      password = entry[2]
      name = entry[3]
      surname = entry[4]

      manager = Manager(id, username, password, name, surname)
      managers.append(manager)
   
   return managers

def create_manager(first_name, last_name):
   cursor = conn.cursor()
   sql = f"""
      INSERT INTO users (username, password, name, surname, is_manager)
      VALUES ('{first_name}', '{last_name}', '{first_name}', '{last_name}', TRUE);
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

# ===========================
# RESIDENTS
# ===========================

def create_resident(first_name, last_name, community):
   cursor = conn.cursor()
   sql = f"""
      INSERT INTO users (username, password, name, surname, community_id)
      VALUES ('{first_name}', '{last_name}', '{first_name}', '{last_name}', {community.id});
   """
   cursor.execute(sql)
   conn.commit()
   cursor.close()

# ===========================
# USERS
# ===========================

def sign_in_user(input_username, input_password):
   cursor = conn.cursor()
   cursor.execute(f"SELECT * FROM users WHERE username = '{input_username}'")
   user_data = cursor.fetchone()
   cursor.close()

   if user_data is None:
      raise ValueError("Invalid credentials")
   
   id = user_data[0]
   username = user_data[1]
   password = user_data[2]
   name = user_data[3]
   surname = user_data[4]
   is_admin = user_data[5]
   is_manager = user_data[6]
   community_id = user_data[7]

   if is_admin:
      user = Admin(id, username, password, name, surname)
   elif is_manager:
      user = Manager(id, username, password, name, surname)
   else:
      user = Resident(id, username, password, name, surname, community_id)

   if not user.is_login_password_valid(input_password):
      raise ValueError("Invalid credentials")

   return user

def delete_user(user):
   cursor = conn.cursor()
   sql = f"DELETE FROM users WHERE id = {user.id}"
   cursor.execute(sql)
   conn.commit()
   cursor.close()

# ===========================
# MAIN
# ===========================

def decide_which_window(user):
   if user.is_admin:
      return open_admin_home_window()
   elif user.is_manager:
      return open_manager_home_window()
   elif user.is_resident is True:
      return open_resident_home_window()   
   else:
      return open_login_window()

def main():
   current_user = None
   current_community = None
   current_service = None
   window = open_login_window()

   while True:
      event, values = window.read()
      if event in (None, "Leave"):
         break

      elif event == "Sign in":
         try:
            username = values["username"]
            password = values["password"]
            current_user = sign_in_user(username, password)
            window.close()
            window = decide_which_window(current_user)
         except Exception as error:

            sg.popup(str(error))

      elif event == "Cancel":
         window.close()
         window = decide_which_window(current_user)

      elif event == "Log out":
         window.close()
         window = open_login_window()

# ===========================
# COMMUNITIES
# ===========================

      elif event == "Communities":
         window.close()
         if current_user.is_admin:
            communities = get_communities()
            window = open_admin_communities_window(communities)
         elif current_user.is_manager:
            communities = get_communities()
            window = open_manager_communities_window(communities)
         else:
            community = get_residents_community(current_user)
            window = open_resident_community_window(community)

      elif event == "Add community":
         window.close()
         window = open_add_community_window()

      elif event == "Create community":
         is_address_filled = (
            values['street_name'] != ""
            and values['house_no'] != ""
            and values['city'] != ""
         )

         if is_address_filled:
            street_name = values["street_name"]
            house_no = values["house_no"]
            city = values["city"]
            create_community(street_name, house_no, city)
            communities = get_communities()
            window.close()
            window = open_admin_communities_window(communities)
         else:
            sg.popup("Enter all fields")

      elif event == "Delete community":
         communities = values["communities"]
         if communities != list():
            delete_community(communities[0])
            communities = get_communities()
            window.close()
            window = open_admin_communities_window(communities)
         else:
            sg.popup("Select a community")
            
      elif event == "Assign service":
         communities = values["communities"]
         if communities != []:
            current_community = communities[0]
            community_services = get_community_services(current_community)
            window.close()
            window = open_add_service_to_community_window(community_services)
         else:
            sg.popup("Select a community")
      
      elif event == "Link service":
         services = get_not_linked_services(current_community)
         window.close()
         window = open_not_linked_services_window(services)
      
      elif event == "Link service to community":
         services = values["services"]
         if services != list():
            link_service_to_community(current_community, services[0])
            community_services = get_community_services(current_community)
            window.close()
            window = open_add_service_to_community_window(community_services)
         else:
            sg.popup("Select a service")
      
      elif event == "Unlink service":
         services = values["services"]
         if services != list():
            unlink_service_from_community(current_community, services[0])
            community_services = get_community_services(current_community)
            window.close()
            window = open_add_service_to_community_window(community_services)
         else:
            sg.popup("Select a service")

      elif event == "Assign resident":
         communities = values["communities"]
         if communities != list():
            current_community = communities[0]
            residents = get_community_residents(current_community)
            window.close()
            window = open_assign_resident_to_community_window(residents)
         else:
            sg.popup("Select a community")

# ===========================
# SERVICES
# ===========================

      elif event == "Services":
         services = get_services()
         window.close()
         window = open_services_window(services)

      elif event == "Add service":
         window.close()
         window = open_add_service_window()

      elif event == "Create service":
         service_name = values["service_name"]
         if service_name:
            create_service(service_name)
            services = get_services()
            window.close()
            window = open_services_window(services)
         else:
            sg.popup("Enter service name")

      elif event == "Delete service":
         services = values["services"]
         if services != list():
            delete_service(services[0])
            services = get_services()
            window.close()
            window = open_services_window(services)
         else:
            sg.popup("Select a service")

      elif event == "Assign service manager":
         services = values["services"]
         if services != list():
            current_service = services[0]
            managers = get_managers()
            window.close()
            window = open_assign_service_manager_window(managers)
         else:
            sg.popup("Select a service")

      elif event == "Assign manager":
         managers = values["managers"]
         if managers != list():
            assign_manager_to_service(current_service, managers[0])
            services = get_services()
            window.close()
            window = open_services_window(services)
         else:
            sg.popup("Select a manager")
      
      elif event == "Manage services":
         communities = values["communities"]
         if communities != list():
            current_community = communities[0]
            services = get_manager_services_for_community(current_community, current_user)
            window.close()
            window = open_manager_services_window(services)
         else:
            sg.popup("Select a community")
      
      elif event == "Assign service price":
         services = values["services"]
         if services != list():
            current_service = services[0]
            window.close()
            window = open_manager_service_price_window()
         else:
            sg.popup("Select a service")

      elif event == "Change service price":
         price = values["price"]
         if price:
            change_community_service_price(current_community, current_service, price)
            services = get_community_services(current_community)
            window.close()
            window = open_manager_services_window(services)
         else:
            sg.popup("Enter a price")
      
      elif event == "View services":
         communities = values["communities"]
         if communities != list():
            current_community = communities[0]
            services = get_community_services(current_community)
            window.close()
            window = open_resident_services_window(services)
         else:
            sg.popup("Select a community")
      
      elif event == "Check service price":
         services = values["services"]
         if services != list():
            price = get_community_service_price(current_community, services[0])
            sg.popup(price)
         else:
            sg.popup("Select a service")

# ===========================
# MANAGERS
# ===========================

      elif event == "Managers":
         managers = get_managers()
         window.close()
         window = open_admin_manager_window(managers)

      elif event == "Add manager":
         window.close()
         window = open_create_manager_window()
      
      elif event == "Create manager":
         first_name = values["first_name"]
         last_name = values["last_name"]
         if first_name and last_name:
            create_manager(first_name, last_name)
            managers = get_managers()
            window.close()
            window = open_admin_manager_window(managers)
         else:
            sg.popup("Enter manager's first name and last name")
      
      elif event == "Delete manager":
         managers = values["managers"]
         if managers == list():
            sg.popup("Select a manager")
         else:
            delete_user(managers[0])
            managers = get_managers()
            window.close()
            window = open_admin_manager_window(managers)

# ===========================
# RESIDENTS
# ===========================

      elif event == "Add resident":
         window.close()
         window = open_create_resident_window()
      
      elif event == "Create resident":
         first_name = values["first_name"]
         last_name = values["last_name"]
         if first_name and last_name:
            create_resident(first_name, last_name, current_community)
            residents = get_community_residents(current_community)
            window.close()
            window = open_assign_resident_to_community_window(residents)
         else:
            sg.popup("Enter resident's first name and last name")
      
      elif event == "Delete resident":
         residents = values["residents"]
         if residents != list():
            delete_user(residents[0])
            residents = get_community_residents(current_community)
            window.close()
            window = open_assign_resident_to_community_window(residents)
         else:
            sg.popup("Select a resident")

   window.close()

if __name__ == "__main__":
   main()

conn.close()
