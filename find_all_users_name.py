from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messages = data['messages']
    users = []
    for message in messages:
        if message.get('actor') == None:
            users.append(message['from'])
        else:
            users.append(message.get('actor'))
    return list(set(users))

if __name__=="__main__":
    data = read_data('data/result.json')
    print(find_all_users_name(data))
