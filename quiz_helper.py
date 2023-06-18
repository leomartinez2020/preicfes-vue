import json
import pprint
import random

tfile = 'ejemplos.txt'

def proc():
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    texto = 'RESPONDA LAS PREGUNTAS 1 A 5 DE ACUERDO CON EL EJEMPLO'
    descripcion = 'Lea las descripciones de la columna de la izquierda (1 - 5). ¿Cuál palabra de la columna de la derecha (A - G) concuerda con cada descripción? La opción H se usa para el ejemplo. Sobran dos palabras más. En las preguntas 1 - 5, marque la letra correcta A - G en su hoja de respuestas'
    quizzes = []
    quiz = {'id': 0, 'slug': '', 'titulo': '', 'tipo': 'tipouno', 'texto': texto, 'descripcion': descripcion, 'tema': '', 'ejempregunta': '', 'preguntas': [], 'palabras': {}}
    pregs = []
    pregd = {}
    #preg = {'texto': '', 'palabra': '', 'letra': '', 'correct': False}
    palabras = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': ''}
    # Procesamiento
    pk = 1
    random.shuffle(letras)
    with open(tfile) as foo:
        for line in foo:
            texto = line.strip()
            if texto.startswith('01)'):
                texto = texto.lstrip('01)')
                quiz['id'] = int(texto)
                quiz['slug'] = 'quiz/' + texto
            elif texto.startswith('02)'):
                texto = texto.lstrip('02)')
                quiz['titulo'] = texto
            elif texto.startswith('03)'):
                texto = texto.lstrip('03)')
                quiz['tema'] = texto
            elif texto.startswith('04)'):
                texto = texto.lstrip('04)')
                quiz['ejempregunta'] = texto
            elif texto.startswith('05)'):
                texto = texto.lstrip('05)')
                palabras['H'] = texto
            elif texto.startswith('06)'):
                texto = texto.lstrip('06)')
                palabras[letras[-1]] = texto
            elif texto.startswith('07)'):
                texto = texto.lstrip('07)')
                palabras[letras[-2]] = texto
            elif texto.startswith('--)'):
                texto = texto.lstrip('--)')
                textos = texto.split(',')
                pregd = {'texto': '', 'palabra': '', 'letra': '', 'correct': False}
                pregd['texto'] = textos[0]
                palabra = textos[1]
                pregd['palabra'] = palabra
                pregd['pk'] = pk
                letra = letras[pk - 1]
                pk += 1
                pregd['letra'] = letra
                palabras[letra] = palabra
                pregs.append(pregd)
    quiz['preguntas'] = pregs
    quiz['palabras'] = palabras
    return json.dumps(quiz, ensure_ascii=False).encode('utf-8')

a = proc()
#pprint.pprint(a.decode())
print(a.decode())
print('=' * 24)
