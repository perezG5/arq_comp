def primo(num):
    if num < 2:
        return False

    for i in range(2,num):
        if num %i == 0:
            return False
        else:
            return True

def sacar_primo(ini, fin):
    a = []
    for i in range(ini, fin):
        if primo(i) == True:
            a.append(i)
    print(a)

print (sacar_primo(0,1000))          

