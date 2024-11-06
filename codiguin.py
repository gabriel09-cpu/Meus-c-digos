import pyautogui 
import time 



#para não perder o controle de sua automação
pyautogui.FAILSAFE = True
#Pausa geral de 0.3 segundos (300 milisegundos)
pyautogui.PAUSE = 0.3 
#Espera um tempo para rodar
time.sleep(5)

#Pegar posição do mouse
#print(pyautogui.position())


#Pegar a resolução da tela
"""print(pyautogui.size())"""

#Clicar com mouse
pyautogui.click(x=484, y=364)

#clicar com botão direito
#pyautogui.click(x=484, y=364, button = "right")

# pyautogui.click(x=484, y=364)

# dois clicks 
#pyautogui.click(x=484 y=364, click = "2")

#mover o mouse
# pyautogui.moveTo(x=610, y=177, duration = 1)
# pyautogui.moveTo(x=1196, y=277, duration=1)
# pyautogui.click(x=1196, y=277)

# pyautogui.scroll(-1500)
# pyautogui.moveTo(x=1022, y=812, duration = 1)
# pyautogui.click(x=1022, y=812)

#funções do teclado
pyautogui.press("win")

# pyautogui.write("clima", interval=0.25)

# pyautogui.press("enter")

#para precionar duas teclas
pyautogui.hotkey("ctrl", "v")


pyautogui.press("enter")

