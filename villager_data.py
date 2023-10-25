"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()

    with open(filename) as file:     

        for line in file:
            species = line.rstrip().split("|")[1]
            unique_species.add(species)
        

    return species


# print(all_species("villagers.csv"))



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    with open(filename) as file:
        
        for line in file:            
            name, specie = line.strip().split("|")[:2]           
            
            if specie == search_string:                
                villagers.append(name )

   
    return sorted(villagers)



# print(get_villagers_by_species("villagers.csv", search_string="Bear"))



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
   
    hobbyes_dict = {}

    with open(filename) as data:
          
        for line in data:
            name, hobby = line.rstrip().split("|")[:4:3]
            if hobby not in hobbyes_dict:
                hobbyes_dict[hobby] = [name]                     
            elif type(hobbyes_dict[hobby]) == list:
                hobbyes_dict[hobby].append(name)
                   
    
    return list(hobbyes_dict.values())

# print(all_names_by_hobby("villagers.csv"))



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    with open(filename) as data:

        for line in data:
            content = line.rstrip().split("|")
            all_data.append(tuple(content))

    return all_data

# print(all_data("villagers.csv"))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """



    with open(filename) as data:

        for line in data:
            content = line.rstrip().split("|")            
            if content[0] == villager_name:                
                return str(content)
        return False
        
# print(find_motto("villagers.csv", "Motto"))



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    dict_by_personality = {}
    with open(filename) as data:               

        for line in data: 
            content = line.rstrip().split("|")         
            name, personality = line.rstrip().split("|")[:3:2]

            if villager_name in content:
                given_personality = content[2]            

            if personality not in dict_by_personality:
                dict_by_personality[personality] = [name]
            elif type(dict_by_personality[personality]) == list:
                dict_by_personality[personality].append(name)   

        return set(dict_by_personality[given_personality])     


# print(find_likeminded_villagers("villagers.csv", "Audie"))