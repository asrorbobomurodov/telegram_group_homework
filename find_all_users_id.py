from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messages = data['messages']
    id_list = []
    for message in messages:
        from_id = message.get('from_id')
        if from_id != None:
            id_list.append(message.get('from_id'))
        else: 
            id_list.append(message.get('actor_id'))
    return list(set(id_list))
data = read_data("data/result.json")
print(find_all_users_id(data))