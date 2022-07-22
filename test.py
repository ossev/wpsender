def probar():
    file = open('C:/Users/admin/projects/wpsender/cargas/carga.txt','r', encoding="utf8")

    for l in file:
        print(l)

if __name__ == '__main__':
    probar()