import os as _0
import yt_dlp as _1

def _2(_3):
    if not _0.path.exists(_3):
        _0.makedirs(_3)

def _4(_5, _6='Carpeta de Descargas I'):
    _2(_6)
    
    _7 = {
        'format': 'best',
        'outtmpl': _0.path.join(_6, '%(title)s [%(id)s].%(ext)s'),
        'noplaylist': True,
        'cachedir': False,
        'no_warnings': True,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        },
    }

    with _1.YoutubeDL(_7) as _8:
        try:
            _9 = _8.extract_info(_5, download=True)
            _A = _8.prepare_filename(_9)
            print(f'Video descargado exitosamente: {_A}')
        except Exception as _B:
            print(f'Ocurrió un error: {_B}')

if __name__ == "__main__":
    _C = "".join([chr(x) for x in [66, 121, 83, 117, 112, 114, 101, 109, 45, 84, 88]])
    print(_C)
    _D = input("Introduce la URL: ")
    _4(_D)
