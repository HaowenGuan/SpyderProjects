#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 


def search(file, city, state):
    """ Read the file and search (city, state)
    """
    txt = open(file, 'r')
    count = 0
    for line in txt:
        line = line.strip()
        line = line.split(',')
        if line[2].lower() == city.lower() and line[3].lower() == state.lower():
            count += 1
            population = float(line[4])
            population = population * 1000
            population = int(population)
            print(line[0] + '\t\t' + line[1] + '\t' + format(population, '10,d'))

    if count == 0:
        print('no results found for {}, {}'.format(city, state))


def main():
    """ main function
    """
    file_name = input("Enter the name of data file: ")
    while True:
        city = input('city: ')
        if city.lower() == 'quit':
            break
        state = input('state abbreviation: ')
        search(file_name, city, state)
                
        