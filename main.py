# importação da biblioteca
import pyautogui as auto
import time

# define espera para cada comando do auto


# abre o menu iniciar
time.sleep(1)
auto.press('win')

# abrir o Google Chrome
time.sleep(2)
auto.write('Chrome')
auto.press('enter')

# maximizar a tela
time.sleep(0.5)
auto.hotkey('alta','space')
auto.press('enter')


# abrir o githubChrome

time.sleep(2)
auto.write('github.com')
auto.press('enter')

# abrir o classroom
time.sleep(3)
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')