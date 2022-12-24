import PySimpleGUI as sg
from user import User
from community import Community
from service import Service
from admin import Admin
from db import conn

# Anonymous windows:____________________________________________________________
def open_anonymous_window():
   anonymous_layout = [
      [sg.Text("Welcome to the system of providing communal services to residents!")],
      [sg.Text("Login as:")],
      [sg.Button("Administrator"), sg.Button("Manager"), sg.Button("Resident"), sg.Button("Leave")]
   ]
   return sg.Window(title="Login portal", layout=anonymous_layout)

def open_login_window():
   login_layout = [
      [sg.Text("Username"), sg.InputText(key="username")],
      [sg.Text("Password"), sg.InputText(key="password", password_char="*")],
      [sg.Button("Sign in"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Login portal", layout=login_layout)

# Admin windows:________________________________________________________________
def open_admin_manage_window():
   admin_manage_layout = [
      [sg.Text("Manage chosen section:")],
      [sg.Button("Communities"), sg.Button("Services"), sg.Button("Managers"), sg.Button("Log out")]
   ]
   return sg.Window(title="Administrator portal", layout=admin_manage_layout)

def open_manage_communities_window():
   communities = communities_list_from_db()
   admin_layout = [
      [sg.Text("Manage community of a particular house:")],
      [sg.Listbox(values=communities, size=(30, len(communities)), key="communities")],
      [sg.Button("Create community"), sg.Button("Delete community"), sg.Button("Manage service"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Administrator portal", layout=admin_layout)

def open_create_community_window():
   create_community_layout = [
      [sg.Text("Street name"), sg.InputText(key="street_name")],
      [sg.Text("House number"), sg.InputText(key="house_no")],
      [sg.Text("City"), sg.InputText(key="city")],
      [sg.Button("Save community"), sg.Button("Return")]
   ]
   return sg.Window(title="Create community", layout=create_community_layout)

def communities_list_from_db():
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

# Save to db windows:___________________________________________________________
def save_community_to_db(values):
   street_name = values["street_name"]
   house_no = values["house_no"]
   city = values["city"]

   cur = conn.cursor()
   cur.execute(
      f"INSERT INTO communities (street_name, house_no, city) \
      VALUES ('{street_name}', '{house_no}', '{city}')"
   )
   conn.commit()
   cur.close()

def save_community_services_to_db(service, community):
   cur = conn.cursor()
   sql = f"""
      INSERT INTO community_services (service_id, community_id)
      VALUES ({service.id}, {community.id});
   """
   cur.execute(sql)
   conn.commit()
   cur.close()

def save_service_to_db(service_id, community_id):
   service_id = service_id["service_id"]
   community_id = community_id[community_id]
   cur = conn.cursor()
   sql = """
   INSERT INTO community_services (service_id, community_id)
   VALUES ({service_id}, {community_id});
   """
   cur.execute(sql)
   conn.commit()
   cur.close()
   print(f"test123: {service_id}")
   print(f"test321")

# Take from db windows__________________________________________________________
def remove_community(community):
   cur = conn.cursor()
   cur.execute(f"DELETE FROM communities WHERE id = {community.id}")
   conn.commit()
   cur.close()

def open_add_service_window(community):
   community_services = community_services_list_from_db(community)
   print("124: ")
   print(community_services)
   admin_add_service_layout = [
      [sg.Text("List of services for chosen community:")],
      [sg.Listbox(values=community_services, size=(30, len(community_services)), key="community_service")],
      [sg.Button("Add service"), sg.Button("Remove service"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Administrator portal", layout=admin_add_service_layout)

def community_services_list_from_db(community):
   cur = conn.cursor()
   sql = f"""
      SELECT s.* FROM services s
      JOIN community_services cs ON cs.service_id = s.id
      WHERE cs.community_id = {community.id};
   """
   cur.execute(sql)
   community_services_list = cur.fetchall()
   cur.close()
   print(community_services_list)
   
   community_services = []

   for service_data in community_services_list:
      id = service_data[0]
      name = service_data[1]
      service = Service(id, name)
      community_services.append(service)
   return community_services

def open_manage_service_window():
   services = services_list_from_db()
   admin_service_layout = [
      [sg.Text("Choose a service to proceed:")],
      [sg.Listbox(values=services, size=(30, len(services)), key="service_name")],
      [sg.Button("Choose and proceed"), sg.Button("Create service"), sg.Button("Delete service"), sg.Button("Add price"), sg.Button("Assign manager"), sg.Button("Cancel")]
   ]
   return sg.Window(title="Administrator portal", layout=admin_service_layout)

def open_create_service_window():
   create_service_layout = [
      [sg.Text("Service name"), sg.InputText(key="name")],
      [sg.Button("Save service"), sg.Button("Return")]
   ]
   return sg.Window(title="Create service", layout=create_service_layout)


def services_list_from_db():
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



def remove_service(service):
   cur = conn.cursor()
   cur.execute(f"DELETE FROM services WHERE id = {service.id}")
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

   if not user.is_login_password_valid(password_value):
      raise ValueError("Invalid credentials")

   return user

def decide_which_window(user):
   if user.is_admin is True:
      return open_admin_manage_window()
   # elif active_user == "manager":
   #    return open_manager_window()
   # elif active_user == "resident":
   #    return open_resident_window()
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

      elif event == "Administrator":
         active_user = "administrator"
         window.close()
         # communities_list_from_db()
         window = open_login_window()
      
      # elif event == "Manager":
      #    active_user = "manager"
      #    window.close()
      #    window = open_login_window()

      # elif event == "Resident":
      #    active_user = "resident"
      #    window.close()
      #    window = open_login_window()

      elif event == "Cancel":
         window.close()
         window = decide_which_window(active_user)

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

      elif event == "Services":
         window.close()
         window = open_manage_service_window()

      elif event == "Go back":
         window.close()

      elif event == "Log out":
         window.close()
         window = open_anonymous_window()

      elif event == "Create community":
         window.close()
         window = open_create_community_window()

      elif event == "Create service":
         window.close()
         window = open_create_service_window()

      elif event == "Save community":
         save_community_to_db(values)
         window.close()
         window = open_manage_communities_window()

      elif event == "Save service":
         
         save_service_to_db(values)
         window.close()
         window = open_manage_service_window()

      elif event == "Manage service":
         community = values["communities"][0]
         if community:
            current_community = community
            window.close()
            window = open_add_service_window(community)
         else:
            sg.popup("Select a community")

      elif event == "Choose and proceed":
         service = values["service_name"][0]
         if service:
            window.close()
            save_community_services_to_db(service, current_community)
            window = open_add_service_window(current_community)

         else:
            sg.popup("Select a service")

      elif event == "Add service":
            window.close()
            window = open_manage_service_window()

      elif event == "Return":
         window.close()
         window = open_manage_communities_window()

      elif event == "Delete community":
         remove_community(values["communities"][0])
         window.close()
         window = open_manage_communities_window()

      elif event == "Delete service":
         remove_service(values["service_name"][0])
         window.close()
         window = open_manage_service_window()

      elif event == "Go back":
         window.close()


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
   window.close()

if __name__ == "__main__":
   main()

conn.close()