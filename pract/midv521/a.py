def filus(fname):
    with open(fname) as file:
        cont = file.readlines()
        if len(cont) != 0:
            print('Good')
            print(len(cont))
        else:
            print('NO')


filus('input.txt')