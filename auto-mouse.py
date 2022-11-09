import pyautogui as pag
import random
import time
import sys
print('Aperte Ctrl-C para sair')

try:
    while True: #! Àrea da tela onde o ponteiro do mosue vai percorrer. Esse valor seta uma área específica onde o ponteiro pode ir, mas pode ser a tela toda também, é só especificar.
        x = random.randint(1, 1080)
        y = random.randint(1, 1080)
        pag.moveTo(x,y,.5) #! .5 é o tempo que o mouse vai demorar pra ir até o lugar de X ou Y. Alterar esse valor altera a velocidade que o ponteiro se desloca.
        time.sleep(.5) #!Tempo que o aplicativo aguarda até fazer o próximo movimento. Alterar esse valor altera o tempo que o aplicativo fica ocioso.
        

except KeyboardInterrupt:
    print('\n')   
