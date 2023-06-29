import datetime
import os.path
import sys
from pathlib import Path
from gtts import gTTS
from pydub import AudioSegment


print('*'*18)
print('Autor: Leonardo Maggiotti')
print('*'*18)
print('Modo de uso:')
print('texto_a_voz_gtts.exe "texto corto"')
print('texto_a_voz_gtts.exe -a [archivo]')
print('')


def procesa_archivo(filename_txt):
    try:
        with open(Path(filename_txt), encoding='utf-8') as f:
            texto_a = f.read()
            return texto_a
    except:
        print('Error al abrir el archivo!')
        sys.exit()


salir = False
texto = ''

try:
    if sys.argv[1] in ('-a', '-A'):
        if Path(sys.argv[2]).exists():
            print('Procesando archivo', sys.argv[2])
            texto = procesa_archivo(sys.argv[2])
        else:
            print('Archivo no encontrado\n')
            salir = True
    else:
        print('Ejecutando por línea de comando')
        if len(sys.argv) > 2:
            print('\n*** El texto debe ir entre comillas ***\n')
            salir = True
        else:
            texto = sys.argv[1]
except:
    print('Sale por default utilizando archivo texto.txt')
    filename_txt = 'texto.txt'
    if not os.path.exists(filename_txt):
        resp = input('El archivo no existe, lo genero? (s/n): ')
        while resp.lower() not in ('s', 'n', 'exit'):
            resp = input('Genero archivo texto.txt? (s/n): ')
        if resp.lower() == 's':
            with open(filename_txt, 'w') as f:
                f.write('')
            print('Agregale tu texto, guardalo y volvé a ejecutar el programa\n')
            os.system(filename_txt)
        sys.exit()
    else:
        texto = procesa_archivo('texto.txt')

if salir:
    sys.exit()

if texto.strip() == '':
    print('No hay texto en el archivo\n')
    sys.exit()

fecha_hora = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename_mp3 = f'audio_{fecha_hora}.mp3'
if not os.path.exists(os.path.join(os.getcwd(), 'audios')):
    try:
        os.mkdir('audios')
        filename_mp3 = f'audios\\audio_{fecha_hora}.mp3'
    except:
        print('No se pudo crear el directorio audios, el archivo quedará junto al ejecutable\n')
else:
    filename_mp3 = f'audios\\audio_{fecha_hora}.mp3'

try:
    gTTS(text=texto, lang='es', slow=False, tld='com.mx').save(filename_mp3)
except:
    print('Error al generar archivo', filename_mp3)
    salir = True
if salir:
    sys.exit()
silence = AudioSegment.silent(duration=500)
new_audio = silence + AudioSegment.from_mp3(filename_mp3)
new_audio.export(filename_mp3, format='mp3')
print('listo!\n')
