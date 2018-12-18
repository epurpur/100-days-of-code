import csv


state = 'NC'

def state_choice(state):
    """Asks for user_state_choice and imports csv('ClimbingAreasCityID.csv') of climbing areas by state. Looks for state in list, then returns list 
    of city_ids and their climbing_area_alias for each location"""
    
    city_id_list = []
    climbing_area_alias = []
    zip_codes = []
    
    with open('ClimbingAreasInfo.csv') as file:
        reader = csv.reader(file)
        my_list = list(reader)
    
    for i in my_list:
        if i[0] == state:
            climbing_area_alias.append(i[2])
            city_id_list.append(i[3])
            zip_codes.append(i[4])
            
    print( city_id_list, climbing_area_alias, zip_codes )
    
state_choice(state)