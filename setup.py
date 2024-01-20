import sys
from cx_Freeze import setup, Executable
 
arquivos = ['fechar-propaganda.png', 'maximizar-janela.png'] 

base = "Win32GUI" if sys.platform == "win32" else None
 

configuracao = Executable(
    script='app.py',
    icon='video.ico', 
    base=base 
)

setup(
    name = 'Bot que baixa arquivo de vídeo.', 
    version = '1.0', 
    description = 'Com esse programa, você pode baixar um video MP4 de 10MB de forma automatizada.',
    author = 'Jonatas L. de Sousa',            
    options = {'build_exe': {'include_files': arquivos,"include_msvcr":True}}, 
    executables = [configuracao]
)