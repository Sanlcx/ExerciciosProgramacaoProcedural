def search_by_name_n_number(n):
    exists = False
    for i in pokedex:
        if n.upper() in i.values():
            exists = True
            for k, v in i.items():
                print(f'{k} > {v}')
                print()
    if not exists:
        print('Pokémon NOT FOUND!')

def search_by_type(n1, n2):
    c = 0
    exists = False
    for i in pokedex:
        if n1.upper() in i.values() and n2 == '':
            exists = True
            c += 1
            for k, v in i.items():
                print(f"{k} > {v}")
                print()
        elif n1.upper() in i.values() and n2.upper() in i.values():
            exists = True
            c += 1
            for k, v in i.items():
                print(f"{k} > {v}")
    if not exists:
        print('No pokémon were found.')
    elif exists and c >= 1:
        print(f"{c} pokémon were found!")


def order(n):
    sorted_pokedex = sorted(pokedex, key=lambda x: x[n])
    for i in sorted_pokedex:
        print(f'{i["Dex Num"]}')
        for k, v in i.items():
            print(f'{k} > {v}')
            print()


def add_or_edit():
    nam = input('Name?\n')
    num = input('Dex number? (XXX)\n')
    t1 = input('Type 1?\n')
    t2 = input('Type 2? (Leave blank if none.)\n')
    if t2 == '':
        pokedex.append({'Name': nam.upper(), 'Dex Num': num, 'Type1': t1.upper()})
    else:
        pokedex.append({'Name': nam.upper(), 'Dex Num': num, 'Type1': t1.upper(), 'Type2': t2.upper()})



def menu():
    print(f'{"POKÉDEX":_^25}')
    print(f'Search By Name or Number {"[1]": >1}')
    print(f'Search By Type {"[2]": >13}')
    print(f'List By Name or Number {"[3]": >5}')
    print(f'Add/Edit Pokémon {"[4]": >11}')
    print(f'{"":_^25}')

pokedex = [
    {
        'Name': 'BULBASAUR',
        'Dex Num': '001',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'IVYSAUR',
        'Dex Num': '002',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'VENUSAUR',
        'Dex Num': '003',
        'Type1': 'GRASS',
        'Type2': 'POISON',
    },
    {
        'Name': 'CHARMANDER',
        'Dex Num': '004',
        'Type1': 'FIRE',
    },
    {
        'Name': 'CHARMELEON',
        'Dex Num': '005',
        'Type1': 'FIRE',
    },
    {
        'Name': 'CHARIZARD',
        'Dex Num': '006',
        'Type1': 'FIRE',
        'Type2': 'FLYING',
    },
    {
        'Name': 'SQUIRTLE',
        'Dex Num': '007',
        'Type1': 'WATER',
    },
    {
        'Name': 'WARTORTLE',
        'Dex Num': '008',
        'Type1': 'WATER',
    },
    {
        'Name': 'BLASTOISE',
        'Dex Num': '009',
        'Type1': 'WATER',
    },

]

going = True
while going:
    menu()
    user_input = int(input('Please choose an option:\n'))
    if user_input == 1:
        op = input("Please type a pokémon's name or dex number\n")
        search_by_name_n_number(op)
    elif user_input == 2:
        op1 = input("Please type the first pokémon's type\n")
        op2 = input("Please type the second pokémon's type (If there ain't one, leave it blank)\n")
        search_by_type(op1, op2)
    elif user_input == 3:
        op = int(input("Would you like to sort by name or number? [1] for Name [2] for Number"))
        if op == 1:
            order('Name')
        elif op == 2:
            order('Dex Num')
    elif user_input == 4:
        add_or_edit()
    else:
        print('Invalid option. Please try again.')
    quit_continue = input('Would you like to quit? Type [y] for yes, anything for no.')
    if quit_continue.upper().strip() == 'Y':
        going = False
