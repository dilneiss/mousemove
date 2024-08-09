import pyautogui
import keyboard
import time


# Função para mover o mouse em uma direção específica
def move_mouse(direction, step=10):
    while True:
        if direction == "up":
            pyautogui.move(0, -step)
        elif direction == "down":
            pyautogui.move(0, step)
        elif direction == "left":
            pyautogui.move(-step, 0)
        elif direction == "right":
            pyautogui.move(step, 0)

        # Verifica se o atalho de interrupção foi pressionado
        if keyboard.is_pressed('esc'):
            print("Movimento interrompido.")
            break

        time.sleep(0.01)  # Ajuste a velocidade do movimento se necessário


# Espera o usuário pressionar uma tecla para começar
print("Pressione as teclas de seta (↑, ↓, ←, →) para mover o mouse. Pressione 'Esc' para parar.")

while True:
    if keyboard.is_pressed('up'):
        move_mouse("up")
    elif keyboard.is_pressed('down'):
        move_mouse("down")
    elif keyboard.is_pressed('left'):
        move_mouse("left")
    elif keyboard.is_pressed('right'):
        move_mouse("right")

    # Aguarda um pequeno intervalo para evitar uso excessivo da CPU
    time.sleep(0.1)
