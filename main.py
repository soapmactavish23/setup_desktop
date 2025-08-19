import pyautogui
import os
from time import sleep
from dotenv import load_dotenv

from funcao_buscar_imagens import clica_na_imagem

load_dotenv()

SENHA_NOTION = os.getenv("SENHA_NOTION")
SENHA_GOOGLE = os.getenv("SENHA_GOOGLE")

# abrir o chrome e daixar na página de busca do google
clica_na_imagem('icone_chrome')
sleep(1)
pyautogui.hotkey("ctrl", "shift", "n")
sleep(2)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("google", interval=0.10)
sleep(1)
pyautogui.press("space")
pyautogui.press("backspace")
pyautogui.press("enter")
sleep(2)
clica_na_imagem("icone_google")
sleep(4)