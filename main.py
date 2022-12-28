import PySimpleGUI as sg
from db import conn
from user import User
from community import Community
from service import Service
from admin import Admin
from manager import Manager

# Anonymous windows:____________________________________________________________
def open_anonymous_window():
   anonymous_layout = [
      [sg.Text("Welcome to the system of providing communal services to residents!")],
      [sg.Text("Login as:")],
      [
         sg.Button("Administrator"),
         sg.Button("Manager"),
         sg.Button("Resident"),
         sg.Button("Leave")
      ]
   ]
   return sg.Window(title="PORTAL 1", layout=anonymous_layout)

def open_login_window():
   login_layout = [
      [sg.Text("Username"), sg.InputText(key="username")],
      [sg.Text("Password"), sg.InputText(key="password", password_char="*")],
      [sg.Button("Sign in"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 2", layout=login_layout)

# Admin windows:________________________________________________________________
def open_admin_manage_window():
   admin_manage_layout = [
      [sg.Text("Manage chosen section:")],
      [
         sg.Button("Communities"),
         sg.Button("Services"),
         sg.Button("Managers"),
         sg.Button("Log out")
      ]
   ]
   return sg.Window(title="PORTAL 3", layout=admin_manage_layout)

def open_manage_communities_window():
   communities = take_communities_from_db()
   admin_layout = [
      [sg.Text("Manage community of a particular house:")],
      [
         sg.Listbox(values=communities,
         size=(30, len(communities)),
         key="communities")
      ],
      [  
         sg.Button("Create community"),
         sg.Button("Delete community"),
         sg.Button("Assign service"),
         sg.Button("Assign resident"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 4", layout=admin_layout)

def open_create_community_window():
   create_community_layout = [
      [sg.Text("Street name"), sg.InputText(key="street_name")],
      [sg.Text("House number"), sg.InputText(key="house_no")],
      [sg.Text("City"), sg.InputText(key="city")],
      [sg.Button("Save community"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 5", layout=create_community_layout)

def open_add_service_window(community):
   community_services = take_community_services_from_db(community)
   admin_add_service_layout = [
      [sg.Text("List of services for chosen community:")],
      [
         sg.Listbox(values=community_services,
         size=(30, len(community_services)),
         key="community_service")
      ],
      [  sg.Button("Add service"),
         sg.Button("Remove service"),
         sg.Button("Assign manager"),
         sg.Button("Cancel")
      ]
   ]
   return sg.Window(title="PORTAL 6", layout=admin_add_service_layout)

def open_manage_service_window():
   services = take_services_from_db()
   admin_service_layout = [
      [sg.Text("Choose a service to proceed:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="service_name")],
      [sg.Button("Choose and proceed"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 7", layout=admin_service_layout)

def open_assign_manager_window():
   # managers = managers_list_from_db() #create managers table db
   admin_managers_layout = [
      [sg.Text("Choose a manager to proceed:")],
      # [sg.Listbox(values=managers, size=(30, len(managers)), key="manager")],
      [sg.Button("Choose and proceed"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 8", layout=admin_managers_layout)

def open_manage_services_window():
   services = take_services_from_db()
   admin_service_layout = [
      [sg.Text("Choose a service to proceed:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="service_name")],
      [sg.Button("Create service"), sg.Button("Delete service"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 11", layout=admin_service_layout)

def open_create_service_window():
   create_service_layout = [
      [sg.Text("Service name"), sg.InputText(key="service_name")],
      [sg.Button("Save service"), sg.Button("Return")]
   ]
   return sg.Window(title="PORTAL 12", layout=create_service_layout)

def open_assign_resident_window(community):
   # community_residents_list = community_residents()
   admin_resident_layout = [
      [sg.Text("Resident(s) of a chosen community:")],
      # [
      #    sg.Listbox(values=community_residents_list,
      #    size=(30, len(community_residents_list)),
      #    key="residents")
      # ],
      [sg.Button("Add resident"), sg.Button("Delete resident"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 9", layout=admin_resident_layout)

def open_create_resident_window():
   create_resident_layout = [
      [sg.Text("First name"), sg.InputText(key="first_name")],
      [sg.Text("Last name"), sg.InputText(key="last_name")],
      [sg.Text("ATTENTION! First name is automatically assigned to be the login name")],
      [sg.Text("and last name to be the password.")],
      [sg.Button("Add"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 10", layout=create_resident_layout)

def open_admin_manager_window():
   # managers_list = get_managers_list()
   admin_resident_layout = [
      [sg.Text("A list containing all managers:")],
      # [
      #    sg.Listbox(values=managers_list,
      #    size=(30, len(managers_list)),
      #    key="managers")
      # ],
      [sg.Button("Add manager"), sg.Button("Delete manager"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 13", layout=admin_resident_layout)

def open_create_resident_window():
   create_resident_layout = [
      [sg.Text("First name"), sg.InputText(key="first_name")],
      [sg.Text("Last name"), sg.InputText(key="last_name")],
      [sg.Text("ATTENTION! First name is automatically assigned to be the login name")],
      [sg.Text("and last name to be the password.")],
      [sg.Button("Add"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 10", layout=create_resident_layout)

def open_create_manager_window():
   create_manager_layout = [
      [sg.Text("First name"), sg.InputText(key="first_name")],
      [sg.Text("Last name"), sg.InputText(key="last_name")],
      [sg.Text("ATTENTION! First name is automatically assigned to be the login name")],
      [sg.Text("and last name to be the password.")],
      [sg.Button("Add"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 14", layout=create_manager_layout)

# Manager windows:
def open_manager_main_window():
   communities = take_communities_from_db()
   manager_layout = [
      [sg.Text("Chose a community to see its services:")],
      [sg.Listbox(values=communities, size=(30, len(communities)),key="communities")],
      [sg.Button("Show services"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 15", layout=manager_layout)

def open_manager_service_window(community):
   community_services = take_community_services_from_db(community)
   manager_choose_service_layout = [
      [sg.Text("List of services for chosen community:")],
      [
         sg.Listbox(values=community_services,
         size=(30, len(community_services)),
         key="community_service")
      ],
      [sg.Button("Assign price"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 16", layout=manager_choose_service_layout)

def open_manager_price_window():
   manager_assign_price_layout = [
      [sg.Text("Charge price for a chosen community's service:")],
      [sg.Text("Price"), sg.InputText(key="service_price")],
      [sg.Button("Charge price"), sg.Button("Cancel")]
   ]
   return sg.Window(title="PORTAL 16", layout=manager_assign_price_layout)

   # Resident window:
   # def open_resident_window():

# Save to db windows:___________________________________________________________
def save_community_to_db(values):
   street_name = values["street_name"]
   house_no = values["house_no"]
   city = values["city"]
   sql = f"""
      INSERT INTO communities (street_name, house_no, city)
      VALUES ('{street_name}', '{house_no}', '{city}');
   """

   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   cur.close()

def save_community_service_to_db(services, community):
   service = services[0]
   sql = f"""
      INSERT INTO community_services (service_id, community_id)
      VALUES ({service.id}, {community.id});
   """

   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   cur.close()

def save_service_to_db(name):
   cur = conn.cursor()
   sql = f"INSERT INTO services (name) VALUES ('{name}');"
   cur.execute(sql)
   conn.commit()
   cur.close()

def save_price_to_db(service, community, price):
   if price == "":
      sg.popup("Enter price")
   else:
      sql = f"""
         UPDATE community_services
         SET price = {price['service_price'].replace(',', '.')}
         WHERE (community_id = '{community[0].id}' AND service_id = '{service}');
      """
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
      cur.close()

# Take from db windows__________________________________________________________
def take_community_services_from_db(community):
   cur = conn.cursor()
   sql = f"""
      SELECT s.* FROM services s
      JOIN community_services cs ON cs.service_id = s.id
      WHERE cs.community_id = {community[0].id};
   """
   cur.execute(sql)
   community_services_list = cur.fetchall()
   cur.close()
   
   community_services = []

   for service_data in community_services_list:
      id = service_data[0]
      name = service_data[1]
      service = Service(id, name)
      community_services.append(service)

   return community_services

def take_communities_from_db():
   cur = conn.cursor()
   cur.execute("SELECT * FROM communities")
   communities_list = cur.fetchall()
   cur.close()
   
   communities = []

   for community in communities_list:
      new_community = Community(
         community[0],
         community[1],
         community[2],
         community[3]
      )
      communities.append(new_community)

   return communities

def take_services_from_db():
   cur = conn.cursor()
   cur.execute("SELECT * FROM services")
   services_list = cur.fetchall()
   cur.close()
   
   services = []

   for service in services_list:
      id = service[0]
      name = service[1]
      service = Service(id, name)
      services.append(service)

   return services

def sign_in_user(values):
   username_value = values["username"]
   password_value = values["password"]

   cur = conn.cursor()
   cur.execute(f"SELECT * FROM users WHERE username = '{username_value}'")
   user_data = cur.fetchone()
   cur.close()

   if user_data is None:
      raise ValueError("Invalid credentials")
   
   id = user_data[0]
   username = user_data[1]
   password = user_data[2]
   name = user_data[3]
   surname = user_data[4]
   is_admin = user_data[5]

   if is_admin is True:
      user = Admin(id, username, password, name, surname)
   
   if is_admin is False:
      user = Manager(id, username, password, name, surname)

   # elif is_manager = True:
   #    user = Manager(id, username, password, name, surname)
   
   # else:
   #    user = Resident(id, username, password, name, surname)

   if not user.is_login_password_valid(password_value):
      raise ValueError("Invalid credentials")

   return user

# Remove from db:_______________________________________________________________
def remove_community(community):
   cur = conn.cursor()
   cur.execute(f"DELETE FROM communities WHERE id = {community.id}")
   conn.commit()
   cur.close()

def remove_service(services):
   service = services[0]
   sql = f"DELETE FROM services WHERE id = {service.id}"

   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   cur.close()

# def open_manager_window():
#    manager_layout = [
#       [sg.Text("Operate on:")],
#       [sg.Button("Prices of community services"), sg.Button("Log out")]
#    ]
#    return sg.Window(title="Manager portal", layout=manager_layout)

# def open_resident_window():
#    resident_layout = [
#       [sg.Text("You are sign in as an resident")],
#       [sg.Button("View service names and prices"), sg.Button("Log out")]
#    ]
#    return sg.Window(title="Resident portal", layout=resident_layout)

def decide_which_window(user):
   if user.is_admin is True:
      return open_admin_manage_window()
   elif user.is_admin is False:
      return open_manager_main_window()
   # elif user.is_resident is True:
      # return open_resident_window()   
   else:
      return open_anonymous_window()

def main():
   active_user = None
   current_community = None
   window = open_anonymous_window()

   while True:
      event, values = window.read()
      if event in (None, "Leave"):
         break

      elif event == "Administrator" or event == "Manager" or event == "Resident":
         window.close()
         window = open_login_window()

      elif event == "Sign in":
         try:
            active_user = sign_in_user(values)
            window.close()
            window = decide_which_window(active_user)
         except Exception as error:
            sg.popup(str(error))

      elif event == "Communities":
         window.close()
         window = open_manage_communities_window()

      elif event == "Create community":
         window.close()
         window = open_create_community_window()

      elif event == "Save community":
         address_filled = (
            values['street_name'] != ""
            and values['house_no'] != ""
            and values['city'] != ""
         )

         if address_filled:
            save_community_to_db(values)
            window.close()
            window = open_manage_communities_window()
         else:
            sg.popup("Enter all fields")

      elif event == "Services":
         window.close()
         window = open_manage_services_window()

      elif event == "Add service":
            window.close()
            window = open_manage_service_window()

      elif event == "Create service":
         window.close()
         window = open_create_service_window()

      elif event == "Save service":
         service_name = values["service_name"]
         if service_name != "":
            save_service_to_db(service_name)
            window.close()
            window = open_manage_services_window()
         else:
            sg.popup("Enter service name")

      elif event == "Choose and proceed":
         services = values["service_name"]
         if services != []:
            window.close()
            save_community_service_to_db(services, current_community)
            window = open_add_service_window(current_community)
         else:
            sg.popup("Select a service")

      elif event == "Assign resident":
         communities = values["communities"]
         if communities != []:
            current_community = communities[0]
            window.close()
            window = open_assign_resident_window(current_community)
         else:
            sg.popup("Select a community")

      elif event == "Assign manager":
         community_service = values["community_service"]
         if community_service != []:
            current_community = communities[0]
            window.close()
            window = open_assign_manager_window()
         else:
            sg.popup("Select a community service first")

      elif event == "Assign service":
         communities = values["communities"]
         if communities != []:
            current_community = communities[0]
            window.close()
            window = open_add_service_window(current_community)
         else:
            sg.popup("Select a community")

      elif event == "Delete community":
         communities = values["communities"]
         if communities != []:
            remove_community(communities[0])
            window.close()
            window = open_manage_communities_window()
         else:
            sg.popup("Select a community")

      elif event == "Delete service":
         services = values["service_name"]
         if services != []:   
            remove_service(services)
            window.close()
            window = open_manage_services_window()
         else:
            sg.popup("Select a service")

      elif event == "Add resident":
         window.close()
         window = open_create_resident_window()

      elif event == "Managers":
         window.close()
         window = open_admin_manager_window()

      elif event == "Add manager":
         window.close()
         window = open_create_manager_window()

      elif event == "Show services":
         communities = values["communities"]
         current_community = communities
         if communities != []:
            window.close()
            window = open_manager_service_window(current_community)
         else:
            sg.popup("Select a community")

      elif event == "Assign price":
         community_services = values["community_service"]
         if community_services != []:
            window.close()
            window = open_manager_price_window()
         else:
            sg.popup("Select a service")

      elif event == "Charge price":
         save_price_to_db(community_services[0].id, current_community, values)
         window.close()
         window = open_manager_service_window(current_community)

      elif event == "Cancel":
         window.close()
         window = decide_which_window(active_user)


      elif event == "Log out":
         window.close()
         window = open_anonymous_window()
      
      elif event == "Return": #portal 5
         window.close()
         window = open_manage_communities_window()

   window.close()

if __name__ == "__main__":
   main()

conn.close()

 #    elif event == "Register":
   #       window.close()
   #       window = open_registration_window()

   #    elif event == "Submit":
   #       try:
   #          logged_in_user = register_user(values)
   #          users.append(logged_in_user)
   #          window.close()
   #          window = decide_which_window()
   #       except Exception as error:
   #          sg.popup(str(error))

   #    elif event == "Save":
   #       try:
   #          edit_user(values)
   #          window.close()
   #          if logged_in_user == admin_user:
   #             window = open_manage_communities_window()
   #          else:
   #             window = open_registered_window()

   #       except Exception as error:
   #          sg.popup(str(error))
      
   #    elif event == "View list of users":
   #       window = open_list_of_users()

   #    elif event == "Delete user":
   #        selected_community = values['user_list'][0]
   #        users.remove(selected_community)
   #        window['user_list'].update(values=users)