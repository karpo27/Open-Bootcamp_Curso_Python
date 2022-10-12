
def numero_primo(x):
    counter = 0
    for i in range(2, x):
        resto = x % i
        if resto == 0:
            counter = counter + 1
        else:
            pass
    if counter == 0:
        return True
    else:
        return False



