
def proc():
    print('Ingrese el tema')
    tema = input()
    print('Ingrese pregunta ejemplo y respuesta ejemplo')
    preg_ejem = input()
    lista_preg = []
    for _ in range(2):
        print('Ingrese definicion y palabra separados por coma')
        preg_resp = input()
        lista_preg.append(preg_resp)
    print('tema', tema)
    print('pregunta ejemplo', preg_ejem)
    print('pregunta-respuesta', lista_preg)

proc()
