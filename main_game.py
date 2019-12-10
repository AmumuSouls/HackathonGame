from qiskit import *

import sys, pygame, random
from pygame import *
from pygame.locals import *
import matplotlib.pyplot as plt
from logic import *

WIN_WIDTH = 1120 - 320
WIN_HEIGHT = 960 - 320
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 0
FLAGS = 0
CAMERA_SLACK = 30

pygame.init()
dimensiones = [800, 640]
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)
pantalla = pygame.display.set_mode(dimensiones)
pantalla2 = pygame.display.set_mode(dimensiones)
imagen_panel = pygame.image.load("img/panel.png")
imagen_boton = pygame.image.load("img/button.png")
imagen_boton_pressed = pygame.image.load("img/buttonPressed.png")
imagen_boton2 = pygame.image.load("img/buttonSquare.png")
imagen_boton_pressed2 = pygame.image.load("img/buttonSquarePressed.png")
imagen_text = pygame.image.load("img/panelInset_brown.png")
player_image = pygame.image.load("img/player.png")
heart = pygame.image.load("img/heart.png")
enemy_image = pygame.image.load("img/heart.png")
botones = []
botonesSeleccion = []
botonesJuego = []
vidas = 3
LEVELNO = 0
attackTurn = 0


class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class GameScene(Scene):
    def __init__(self, levelno):
        super(GameScene, self).__init__()
        self.bg = Surface((32,32))
        self.bg.convert()
        self.bg.fill(Color("#0094FF"))
        circuito = MONSTERS[levelno-1]
        circuitoInter = circuito.draw(output='mpl')
        circuitoInter.savefig('img/histogram.png')
        circuitoInter.clf()
        plt.close('all')

    def render(self, screen):
        screen.fill((150, 150, 150))

        enemy_image = pygame.image.load("img/histogram.png")
        r_boton_1_1 = imagen_boton.get_rect()
        r_boton_1_2 = imagen_boton.get_rect()
        r_boton_1_3 = imagen_boton.get_rect()
        r_boton_1_4 = imagen_boton.get_rect()
        r_boton_1_5 = imagen_boton.get_rect()
        r_boton_1_6 = imagen_boton.get_rect()
        r_boton_1_7 = imagen_boton.get_rect()
        r_boton_1_1.center = [180, 460]
        botonesJuego.append(
            {'texto': "Espada_0", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1,
             'on_click': False})
        r_boton_1_2.center = [180, 520]
        botonesJuego.append(
            {'texto': "Espada_1", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_2,
             'on_click': False})
        r_boton_1_3.center = [400, 460]
        botonesJuego.append(
            {'texto': "Espada_+", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_3,
             'on_click': False})
        r_boton_1_4.center = [400, 520]
        botonesJuego.append(
            {'texto': "Espada_-", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_4,
             'on_click': False})
        r_boton_1_5.center = [620, 460]
        botonesJuego.append(
            {'texto': "Espada_horario", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_5,
             'on_click': False})
        r_boton_1_6.center = [620, 520]
        botonesJuego.append(
            {'texto': "Espada_antihor", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_6,
             'on_click': False})
        r_boton_1_7.center = [400, 580]
        botonesJuego.append(
            {'texto': "Espada entrelaz", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_7,
             'on_click': False})
        player = pygame.transform.scale(player_image, [300, 200])
        enemy = pygame.transform.scale(enemy_image, [300, 150])
        heart1 = pygame.transform.scale(heart, [50, 50])
        heart2 = pygame.transform.scale(heart, [50, 50])
        heart3 = pygame.transform.scale(heart, [50, 50])
        panel = pygame.transform.scale(imagen_panel, [760, 220])
        pantalla.blit(heart1, [20, 20])
        if vidas >= 2:
            pantalla.blit(heart2, [80, 20])
        if vidas == 3:
            pantalla.blit(heart3, [140, 20])
        pantalla.blit(enemy, [400, 200])
        pantalla.blit(player, [20, 200])
        pantalla.blit(panel, [20, 400])
        draw_initial_buttons(botonesJuego)

    def update(self):
        pass

    def exit(self):
        self.manager.go_to(CustomScene("You win!"))

    def die(self):
        self.manager.go_to(CustomScene("You lose!"))

    def weaponLogic(self, array, counts, result):
        if len(array) == 1:
            if array[0] == '1':
                if counts['1'] == 1000:
                    self.manager.go_to(CustomScene("Has fallado!"))
            else:
                print("Has acertado, prueba otros niveles")
                self.manager.go_to(CustomScene("Bien hecho!"))
        else:
            print("El valor de la parte_0 es:", counts['0'], ", el valor de la parte 1 es: ", counts['1'])
            porcentaje = counts['0']
            print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            if array[0] == '1':
                print("Has fallado, vuelve a intentarlo")
                self.manager.go_to(CustomScene("Has fallado!"))

            else:
                print("Has acertado con una probabilidad de ", porcentaje, ", prueba otros niveles")
                self.manager.go_to(CustomScene("Has acertado con una probabilidad de ", porcentaje, ", prueba otros niveles"))

    def suerte(self, array, porcentaje):
        if array[0] == '0':
            print("Has fallado, vuelve a intentarlo")
            self.manager.go_to(CustomScene("Has fallado!"))

        else:
            print("Has acertado con una probabilidad de ", porcentaje, ", prueba otros niveles")
            self.manager.go_to(CustomScene("Bien hecho, has tenido suerte!"))

    def weaponLogic2(self, array, counts, result):
        if len(array) == 1:
            if array[0] == '01':
                if counts['01'] == 1000:
                    print("Has fallado, vuelve a intentarlo")
                    self.manager.go_to(CustomScene("Has fallado!"))
            elif array[0] == '00':
                print("Has acertado, prueba otros niveles")
                self.manager.go_to(CustomScene("Bien hecho!"))
            elif array[0] == '10':
                print("Has fallado, vuelve a intentarlo")
                self.manager.go_to(CustomScene("Has fallado!"))
            else:
                print("Has fallado, vuelve a intentarlo")
                self.manager.go_to(CustomScene("Has fallado!"))
        elif len(array) == 2:
            if array[0] == '00':
                if array[1] == '01':
                    print("El valor del '00' es:", counts['00'], ", el valor del '01' es: ", counts['01'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
                if array[1] == '10':
                    print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
                if array[1] == '11':
                    print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
            if array[1] == "00":
                if array[0] == '01':
                    print("El valor del '00' es:", counts['00'], ", el valor del '01' es: ", counts['01'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
                if array[0] == '10':
                    print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
                if array[0] == '11':
                    print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                    porcentaje = counts['00']
                    print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
        else:
            porcentaje = counts['00']
            porcentaje = porcentaje / 10
            if array[0] == '00':
                print("El valor del '00' es:", counts['00'])
                if array[1] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[1] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[1] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[2] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[2] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[2] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[3] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[3] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[3] == '11':
                    print("El valor del '11' es:", counts['11'])
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
            elif array[1] == '00':
                print("El valor del '00' es:", counts['00'])
                if array[0] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[0] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[0] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[2] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[2] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[2] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[3] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[3] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[3] == '11':
                    print("El valor del '11' es:", counts['11'])
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
            elif array[2] == '00':
                print("El valor del '00' es:", counts['00'])
                if array[0] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[0] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[0] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[1] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[1] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[1] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[3] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[3] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[3] == '11':
                    print("El valor del '11' es:", counts['11'])
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)
            elif array[3] == '00':
                print("El valor del '00' es:", counts['00'])
                if array[0] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[0] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[0] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[2] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[2] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[2] == '11':
                    print("El valor del '11' es:", counts['11'])
                if array[1] == '01':
                    print("El valor del '01' es:", counts['01'])
                if array[1] == '10':
                    print("El valor del '10' es:", counts['10'])
                if array[1] == '11':
                    print("El valor del '11' es:", counts['11'])
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
                array = dic_to_array(counts)
                self.suerte(array, porcentaje)

    def handle_events(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                mouse = e.pos
                for boton in botonesJuego:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if e.type == MOUSEBUTTONUP:
                for boton in botonesJuego:
                    if boton['on_click']:
                        if boton['texto'] == "Espada_0":
                            print(main.LEVELNO)
                            try:
                                if main.LEVELNO < 8:
                                    result = qubit1function(main.LEVELNO-1, 0)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic(array, counts, result)
                                else:
                                    if main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[0]
                                        main.attackTurn = 1
                                    elif main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[0]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")


                        elif boton['texto'] == "Espada_1":
                            try:

                                if main.LEVELNO <8:
                                    result = qubit1function(main.LEVELNO-1, 1)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic(array, counts, result)
                                else:
                                    if  main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[1]
                                        main.attackTurn = 1
                                    elif  main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[1]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")
                        elif boton['texto'] == "Espada_+":
                            try:
                                if main.LEVELNO < 8:
                                    result = qubit1function(main.LEVELNO-1, 2)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic(array, counts, result)
                                else:
                                    if  main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[2]
                                        main.attackTurn = 1
                                    elif  main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[2]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")

                        elif boton['texto'] == "Espada_-":
                            try:
                                if main.LEVELNO < 8:
                                    result = qubit1function(main.LEVELNO-1, 3)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic( array, counts, result)
                                else:
                                    if  main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[3]
                                        main.attackTurn = 1
                                    elif  main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[3]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")
                        elif boton['texto'] == "Espada_horario":
                            try:
                                if main.LEVELNO < 8:
                                    result = qubit1function(main.LEVELNO-1, 4)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic(array, counts, result)
                                else:
                                    if  main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[4]
                                        main.attackTurn = 1
                                    elif  main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[4]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")
                        elif boton['texto'] == "Espada_antihor":
                            try:
                                if main.LEVELNO <8:
                                    result = qubit1function(main.LEVELNO-1, 5)
                                    counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                     shots=1000).result().get_counts()
                                    array = dic_to_array(counts)
                                    self.weaponLogic(array, counts, result)
                                else:
                                    if main.attackTurn == 0:
                                        sword2 = setsword2(0)
                                        result = MONSTERS[main.LEVELNO-1] + sword2[5]
                                        main.attackTurn = 1
                                    elif main.attackTurn == 1:
                                        sword2 = setsword2(1)
                                        result = result + sword2[5]
                                        counts = execute(result, Aer.get_backend('qasm_simulator'),
                                                         shots=1000).result().get_counts()
                                        array = dic_to_array(counts)
                                        main.attackTurn = 0
                                        self.weaponLogic2(array, counts, result)
                            except:
                                print("El circuito no es valido")
                        elif boton['texto'] == "Espada entrelazada":
                            resultado = godsword(MONSTERS[main.LEVELNO-1])
                            if resultado == 1:
                                print("Has acertado, prueba otros niveles")
                                self.manager.go_to(GameSelectionScene())
                            else:
                                print("Has fallado, vuelve a intentarlo")
                                self.manager.go_to(GameSelectionScene())
                    boton['on_click'] = False


class GameSelectionScene(Scene):
    def __init__(self):
        super(GameSelectionScene, self).__init__()
        self.bg = Surface((32,32))
        self.bg.convert()
        self.bg.fill(Color("#0094FF"))

    def render(self, screen):
        screen.fill((0, 200, 0))

        r_boton_1_1 = imagen_boton.get_rect()
        r_boton_1_2 = imagen_boton.get_rect()
        r_boton_1_1.center = [150, 100]
        botonesSeleccion.append(
            {'texto': "1", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_1,
             'on_click': False})
        r_boton_1_2.center = [210, 100]
        botonesSeleccion.append(
            {'texto': "2", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_2,
             'on_click': False})

        r_boton_1_3 = imagen_boton.get_rect()
        r_boton_1_4 = imagen_boton.get_rect()
        r_boton_1_3.center = [270, 100]
        botonesSeleccion.append(
            {'texto': "3", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_3,
             'on_click': False})
        r_boton_1_4.center = [330, 100]
        botonesSeleccion.append(
            {'texto': "4", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_4,
             'on_click': False})

        r_boton_1_5 = imagen_boton.get_rect()
        r_boton_1_6 = imagen_boton.get_rect()
        r_boton_1_5.center = [390, 100]
        botonesSeleccion.append(
            {'texto': "5", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_5,
             'on_click': False})
        r_boton_1_6.center = [450, 100]
        botonesSeleccion.append(
            {'texto': "6", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_6,
             'on_click': False})

        r_boton_1_7 = imagen_boton.get_rect()
        r_boton_1_8 = imagen_boton.get_rect()
        r_boton_1_7.center = [510, 100]
        botonesSeleccion.append(
            {'texto': "7", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_7,
             'on_click': False})
        r_boton_1_8.center = [570, 100]
        botonesSeleccion.append(
            {'texto': "8", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_8,
             'on_click': False})

        r_boton_1_9 = imagen_boton.get_rect()
        r_boton_1_10 = imagen_boton.get_rect()
        r_boton_1_9.center = [630, 100]
        botonesSeleccion.append(
            {'texto': "9", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_9,
             'on_click': False})
        r_boton_1_10.center = [700, 100]
        botonesSeleccion.append(
            {'texto': "10", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_10,
             'on_click': False})

        r_boton_1_11 = imagen_boton.get_rect()
        r_boton_1_12 = imagen_boton.get_rect()
        r_boton_1_11.center = [150, 200]
        botonesSeleccion.append(
            {'texto': "11", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_11,
             'on_click': False})
        r_boton_1_12.center = [210, 200]
        botonesSeleccion.append(
            {'texto': "12", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_12,
             'on_click': False})

        r_boton_1_13 = imagen_boton.get_rect()
        r_boton_1_13.center = [270, 200]
        botonesSeleccion.append(
            {'texto': "13", 'imagen': imagen_boton2, 'imagen_pressed': imagen_boton_pressed2, 'rect': r_boton_1_13,
             'on_click': False})

        pantalla.fill(FONDO)
        panel = pygame.transform.scale(imagen_panel, [760, 600])
        pantalla.blit(panel, [20, 20])
        draw_initial_buttons(botonesSeleccion)

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                mouse = e.pos
                for boton in botonesSeleccion:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if e.type == MOUSEBUTTONUP:
                for boton in botonesSeleccion:
                    if boton['on_click']:
                        if boton['texto'] == "1":
                            main.LEVELNO = 1
                            self.manager.go_to(GameScene(1))
                        elif boton['texto'] == "2":
                            main.LEVELNO = 2
                            self.manager.go_to(GameScene(2))
                        elif boton['texto'] == "3":
                            main.LEVELNO = 3
                            self.manager.go_to(GameScene(3))
                        elif boton['texto'] == "4":
                            main.LEVELNO = 4
                            self.manager.go_to(GameScene(4))
                        elif boton['texto'] == "5":
                            main.LEVELNO = 5
                            self.manager.go_to(GameScene(5))
                        elif boton['texto'] == "6":
                            main.LEVELNO = 6
                            self.manager.go_to(GameScene(6))
                        elif boton['texto'] == "7":
                            main.LEVELNO = 7
                            self.manager.go_to(GameScene(7))
                        elif boton['texto'] == "8":
                            main.LEVELNO = 8
                            self.manager.go_to(GameScene(8))
                        elif boton['texto'] == "9":
                            main.LEVELNO = 9
                            self.manager.go_to(GameScene(9))
                        elif boton['texto'] == "10":
                            main.LEVELNO = 10
                            self.manager.go_to(GameScene(10))
                        elif boton['texto'] == "11":
                            main.LEVELNO = 11
                            self.manager.go_to(GameScene(11))
                        elif boton['texto'] == "12":
                            main.LEVELNO = 12
                            self.manager.go_to(GameScene(12))
                        elif boton['texto'] == "13":
                            main.LEVELNO = 13
                            self.manager.go_to(GameScene(13))
                    boton['on_click'] = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                self.manager.go_to(TitleScene())


class CustomScene(object):

    def __init__(self, text):
        self.text = text
        super(CustomScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)

    def render(self, screen):
        # ugly!
        screen.fill((0, 200, 0))
        text1 = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text1, (200, 50))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.manager.go_to(GameSelectionScene())


class TitleScene(object):

    def __init__(self):

        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def render(self, screen):
        screen.fill((0, 200, 0))
        input_text = pygame.transform.scale(imagen_text, [440, 50])

        r_boton_1_1 = imagen_boton.get_rect()
        r_boton_1_2 = imagen_boton.get_rect()
        input_text_rect = input_text.get_rect()
        input_text_rect.center = [400, 100]
        campo_texto = {'imagen': input_text, 'rect': input_text_rect}
        texto_entrada = "Hackthon Game"
        r_boton_1_1.center = [400, 270]
        botones.append(
            {'texto': "Exit", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1,
             'on_click': False})
        r_boton_1_2.center = [400, 200]
        botones.append(
            {'texto': "Play", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_2,
             'on_click': False})
        pantalla.fill(FONDO)
        panel = pygame.transform.scale(imagen_panel, [760, 600])
        pantalla.blit(panel, [20, 20])
        draw_initial_buttons(botones)
        pantalla.blit(input_text, campo_texto['rect'].topleft)
        set_text(campo_texto, texto_entrada)

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == MOUSEBUTTONDOWN:
                mouse = e.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if e.type == MOUSEBUTTONUP:
                for boton in botones:
                    if boton['on_click']:
                        if boton['texto'] == "Play":
                            self.manager.go_to(GameSelectionScene())
                        elif boton['texto'] == "Exit":
                            pygame.quit()
                    boton['on_click'] = False


class SceneMananger(object):
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])


def draw_initial_buttons(lista_botones):

    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)


def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)


def main():
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Hackathon Game")
    timer = pygame.time.Clock()
    running = True
    manager = SceneMananger()
    setMonsters()
    setWeapons()

    while running:
        timer.tick(60)
        if pygame.event.get(QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()