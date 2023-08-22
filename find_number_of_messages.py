from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    n = len(data['messages'])
    return n

if __name__== "__main__":
    data = read_data('data/result.json')
    print(find_number_of_messages(data))