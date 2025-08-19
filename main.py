import pyautogui
import os
from time import sleep
from dotenv import load_dotenv

from funcao_buscar_imagens import clica_na_imagem

load_dotenv()

SENHA_NOTION = os.getenv("SENHA_NOTION")
SENHA_GOOGLE = os.getenv("SENHA_GOOGLE")