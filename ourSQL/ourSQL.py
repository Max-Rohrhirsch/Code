#######################################
# USAGE
#######################################
'''
import ourSQL

ourSQL.query('commands')

'''
#######################################
# IMPORTS
#######################################
import os


#######################################
# MAIN CODE
#######################################

def query(_commands):
    commands = _commands.split(';')

    for command in commands:
        words = command.split()
        if words[0].lower() == 'create':
            file = open(f'./ourSQL/DB_{words[1]}', 'w+')
            if words[2][0] == '(' and words[-1][-1] == ')':
                text = ' '.join(words[2:])[1:-1]
                file.write(text)
        elif words[0].lower() == 'delete':
            os.remove(f'./ourSQL/DB_{words[1]}')

            # HARD PART

        elif words[0].lower() == 'insert':
            file = open(f'./ourSQL/DB_{words[1]}', 'a+')
            file.write(' '.join(words[2:]))
        elif words[0].lower() == 'select':
            pass
        else:
            print(command)






#######################################
# RUN/ TEST
#######################################

if __name__ == '__main__':
    # query('insert into main values ((1, 2), (3, 4))')
    query('create main (column1 column2)')
