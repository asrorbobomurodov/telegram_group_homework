from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    messages_count = {}
    
    for user in id_list:
        messages_count[user] = 0
        
    for msg in data['messages']:
        from_id = msg.get('from_id')
        
        if from_id == None:
            actor_id = msg.get('actor_id')
            messages_count[actor_id] += 1
        else:
            messages_count[from_id] += 1
    
    return messages_count
if __name__ == "__main__":
    data = read_data('data/result.json')
    id_list = find_all_users_id(data)
    messages_count = find_user_message_count(data, id_list)
    print(messages_count)