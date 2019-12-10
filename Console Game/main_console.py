from random import randint

from qiskit import *
from matplotlib import pyplot as plt
import numpy as np
from qiskit import *
from random import seed

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np
WEAPONS = []
MONSTERS = []


def setWeapons():

    zerosword = QuantumCircuit(1, 1)
    zerosword.measure(0, 0)
    WEAPONS.append(zerosword)
    onesword = QuantumCircuit(1, 1)
    onesword.x(0)
    onesword.measure(0, 0)
    WEAPONS.append(onesword)
    plussword = QuantumCircuit(1, 1)
    plussword.h(0)
    plussword.measure(0, 0)
    WEAPONS.append(plussword)

    minussword = QuantumCircuit(1, 1)
    minussword.h(0)
    minussword.x(0)
    minussword.measure(0, 0)
    WEAPONS.append(minussword)

    y0sword = QuantumCircuit(1, 1)
    y0sword.sdg(0)
    y0sword.h(0)
    y0sword.measure(0, 0)
    WEAPONS.append(y0sword)

    y1sword = QuantumCircuit(1, 1)
    y1sword.sdg(0)
    y1sword.h(0)
    y1sword.x(0)
    y1sword.measure(0, 0)
    WEAPONS.append(y1sword)
def setsword2(i):
## qubit2
    WEAPONS1 = []
    zerosword = QuantumCircuit(2, 2)
    zerosword.measure(i, i)
    WEAPONS1.append(zerosword)
    onesword = QuantumCircuit(2, 2)
    onesword.x(i)
    onesword.measure(i, i)
    WEAPONS1.append(onesword)
    plussword = QuantumCircuit(2, 2)
    plussword.h(i)
    plussword.measure(i, i)
    WEAPONS1.append(plussword)
    minussword = QuantumCircuit(2, 2)
    minussword.h(i)
    minussword.x(i)
    minussword.measure(i, i)
    WEAPONS1.append( minussword)
    y0sword = QuantumCircuit(2, 2)
    y0sword.sdg(i)
    y0sword.h(i)
    y0sword.measure(i, i)
    WEAPONS1.append(y0sword)
    y1sword = QuantumCircuit(2, 2)
    y1sword.sdg(i)
    y1sword.h(i)
    y1sword.x(i)
    y1sword.measure(i, i)
    WEAPONS1.append(y1sword)
    return WEAPONS1


def setMonsters():
    zero = QuantumCircuit(1, 1)
    MONSTERS.append(zero)

    one = QuantumCircuit(1, 1)
    one.x(0)
    MONSTERS.append(one)
    plus = QuantumCircuit(1, 1)
    plus.h(0)
    MONSTERS.append(plus)
    minus = QuantumCircuit(1, 1)
    minus.x(0)
    minus.h(0)
    MONSTERS.append(minus)
    y0 = QuantumCircuit(1, 1)
    y0.h(0)
    y0.s(0)
    MONSTERS.append(y0)
    y1 = QuantumCircuit(1, 1)
    y1.x(0)
    y1.h(0)
    y1.s(0)
    MONSTERS.append(y1)

    a_dict = {1: zero, 2: one, 3: plus, 4: minus, 5: y0, 6: y1}

    randomenemy = QuantumCircuit(1)
    v = QuantumCircuit(1)

    for n in range(3):

        value = randint(0, 7)

        if value > 6 or value == 0:
            pass

        else:
            v = randomenemy + a_dict[value]
            randomenemy = v
            v = 0
    MONSTERS.append(randomenemy)
    #qubits de 2
    conx01 = QuantumCircuit(2, 2)
    conx01.cx(0, 1)
    conx01.draw(output='mpl')
    conx10 = QuantumCircuit(2, 2)
    conx10.cx(1, 0)
    conx10.draw(output='mpl')
    swap = QuantumCircuit(2, 2)
    swap.cx(0, 1)
    swap.cx(1, 0)
    swap.cx(0, 1)
    swap.draw(output='mpl')
    conz01 = QuantumCircuit(2, 2)
    conz01.cz(0, 1)
    conz01.draw(output='mpl')
    conz10 = QuantumCircuit(2, 2)
    conz10.cz(1, 0)
    conz10.draw(output='mpl')



    conx01random = rnot2qb(conx01)
    MONSTERS.append(conx01random)
    conx10random = rnot2qb(conx10)
    MONSTERS.append(conx10random)
    swaprandom = rnot2qb(swap)
    MONSTERS.append(swaprandom )
    conz01random = rnot2qb(conz01)
    MONSTERS.append(conz01random)
    conz10random = rnot2qb(conz10)
    MONSTERS.append(conz10random)

    entanglement = QuantumCircuit(2, 2)
    entanglement.h(0)
    entanglement.cx(0, 1)
    entanglement.draw(output='mpl')
    entanglementrandom = rnot2qb(entanglement)
    MONSTERS.append(entanglementrandom)

def rnot2qb(monster):
    hloop = QuantumCircuit(2, 2)
    for n in range(2):
        value = randint(1, 2)
        # print(value)
        # print(n)
        if value == 1:
             hloop.x(n)
        else:
                pass
        the_answer = hloop + monster
    return the_answer

def armas(qubit2):
    print("0.espada_0")

    print("1.espada_1")

    print("2.espada_+")

    print("3.espada_-")

    print("4.espada_horario")

    print("5.espada_antihorario")
    if qubit2 ==1:
        print("6.entanglement_sword")

def dic_to_array(dic):
    array=[]
    for key in dic.keys():
        array.append(key)

    return array
def  inicio():
    print("Bienvenido a HackthonGame")
    print("Menu:\n1.Start \n2.Exit")

def suerte(array,nombre,porcentaje):
    if array[0] == '0':
        print("Has acertado con una probabilidad de ", porcentaje, ", prueba otros niveles")
        niveles(nombre)

    else:
        print("Has fallado, vuelve a intentarlo")
        niveles(nombre)

def logicaqubit2(array,counts,nombre,result):
    if len(array) == 1:
        if array[0] == '01':
            if counts['01'] == 1000:
                print("Has fallado, vuelve a intentarlo")
                niveles(nombre)
        elif array[0] == '00':
            print("Has acertado, prueba otros niveles")
            niveles(nombre)
        elif array[0] == '10':
            print("Has fallado, vuelve a intentarlo")
            niveles(nombre)
        else:
            print("Has fallado, vuelve a intentarlo")
            niveles(nombre)
    elif len(array)==2:
        if array[0] == '00':
            if array[1] == '01':
                print("El valor del '00' es:", counts['00'], ", el valor del '01' es: ", counts['01'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
            if array[1] == '10':
                print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
            if array[1] == '11':
                print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
        if array[1]=="00":
            if array[0] == '01':
                print("El valor del '00' es:", counts['00'], ", el valor del '01' es: ", counts['01'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
            if array[0] == '10':
                print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
            if array[0] == '11':
                print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                porcentaje = counts['00']
                porcentaje = porcentaje / 10
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)
            suerte(array, nombre, porcentaje)
    else:
        porcentaje = counts['00']
        porcentaje = porcentaje / 10
        if array[0]=='00':
            print("El valor del '00' es:", counts['00'])
            if array[1]=='01':
                print("El valor del '01' es:", counts['01'])
            if array[1]=='10':
                print("El valor del '10' es:", counts['10'])
            if array[1]=='11':
                print("El valor del '11' es:", counts['11'])
            if array[2]=='01':
                print("El valor del '01' es:", counts['01'])
            if array[2]=='10':
                print("El valor del '10' es:", counts['10'])
            if array[2]=='11':
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
            suerte(array,nombre,porcentaje)
        elif array[1]=='00':
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
            suerte(array, nombre, porcentaje)
        elif array[2]=='00':
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
            suerte(array, nombre, porcentaje)
        elif array[3]=='00':
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
            suerte(array, nombre, porcentaje)
def logicaqubit1(array,nombre,counts,result):
    if len(array) == 1:
        if array[0] == '1':
            if counts['1'] == 1000:
                print("Has fallado, vuelve a intentarlo")
                niveles(nombre)
        else:
            print("Has acertado, prueba otros niveles")
            niveles(nombre)
    else:
        print("El valor de la parte_0 es:", counts['0'], ", el valor de la parte 1 es: ", counts['1'])
        porcentaje = counts['0']
        porcentaje=porcentaje/10
        print("El arma no ha sido la correcta,vamos a probar si has tenido suerte")
        counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
        array = dic_to_array(counts)
        if array[0] == '0':
            print("Has acertado con una probabilidad de ", porcentaje, ", prueba otros niveles")
            niveles(nombre)

        else:
            print("Has fallado, vuelve a intentarlo")
            niveles(nombre)


def godsword(code):
    measurexd = QuantumCircuit(2, 2)
    measurexd.measure(0, 0)
    measurexd.measure(1, 1)

    code2 = code + measurexd

    counts = execute(code2, Aer.get_backend('qasm_simulator')).result().get_counts()

    temp = []
    diclist = []
    n = 0
    out = 78

    for key in counts.items():
        n = n + 1
        temp = [key[0]]
        diclist.append(temp)

    #print(diclist)
    if len(diclist) == 2:
        if ['11'] in diclist:
            if ['00'] in diclist:
                out = 1

            else:
                out = 0

        elif ['10'] in diclist:
            if ['01'] in diclist:
                out = 1

            else:
                out = 0

        else:
            out = 0

    else:
        out = 0

    return out
def niveles(nombre):
    vida=3
    if nombre=="1":
        print("Bienvenido al browser de niveles")
        print("Pulse del 1 al 13 para acceder a los niveles y el 14 para salir")
        nivel=input()
        nivelInt=int(nivel)

        if nivelInt==1:
            print("Has selecionado el 1º nivel")

            print(MONSTERS[0].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[0] + WEAPONS[int(arma)]

            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array,nombre,counts,result)
        if nivelInt == 2:
            print("Has selecionado el 2º nivel")
            print(MONSTERS[1].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[1] + WEAPONS[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 3:
            print("Has selecionado el 3ª nivel")
            print(MONSTERS[2].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[2] + WEAPONS[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 4:
            print("Has selecionado el 4ª nivel")
            print(MONSTERS[3].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima.  Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[3] + WEAPONS[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 5:
            print("Has selecionado el 5º nivel")
            print(MONSTERS[4].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[4] + WEAPONS[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 6:
            print("Has selecionado el 6º nivel")
            print(MONSTERS[5].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[5] + WEAPONS[int(arma)]

            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 7:
            print("Has selecionado el 7º nivel")
            print(MONSTERS[6].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
            armas(0)

            print("Elige el arma que veas correcta,desde el 0 al 5")
            arma = input()
            result = MONSTERS[6] + WEAPONS[int(arma)]

            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit1(array, nombre, counts, result)
        if nivelInt == 8:
            print("Has selecionado el 8º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[7].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6")
            armas(1)

            print("Elige tu primer arma")
            arma = input()
            if int(arma)==6:
                resultado= godsword(MONSTERS[7])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2= setsword2(0)
                result = MONSTERS[7] + sword2[int(arma)]
                print("Elige tu segunda arma")
                arma =input()
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt == 9:
            print("Has selecionado el 9º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[8].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6")
            armas(1)
            print("Elige tu primer arma")
            arma = input()
            if int(arma)==6:
                resultado=godsword(MONSTERS[8])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2= setsword2(0)
                result = MONSTERS[8] + sword2[int(arma)]
                print("Elige tu segunda arma")
                arma =input()
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt == 10:
            print("Has selecionado el 10º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[9].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6")
            armas(1)
            print("Elige tu primer arma")
            arma = input()
            if int(arma) ==6:
                resultado=godsword(MONSTERS[9])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2= setsword2(0)
                result = MONSTERS[9] + sword2[int(arma)]
                print("Elige tu segunda arma")
                arma =input()
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt == 11:
            print("Has selecionado el 11º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[10].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6")
            armas(1)
            print("Elige tu primer arma")
            arma = input()
            if int(arma) ==6:
                resultado=godsword(MONSTERS[10])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2= setsword2(0)
                result = MONSTERS[10] + sword2[int(arma)]
                print("Elige tu segunda arma")
                arma =input()
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt == 12:
            print("Has selecionado el 12º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[11].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6")
            armas(1)
            print("Elige tu primer arma")
            arma = input()
            if int(arma)==6:
                resultado =godsword(MONSTERS[11])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2= setsword2(0)
                result = MONSTERS[11] + sword2[int(arma)]
                print("Elige tu segunda arma")
                arma =input()
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt == 13:
            print("Has selecionado el 13º nivel")
            print("Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
            print(MONSTERS[12].draw())
            print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 6 ")
            armas(1)
            print("Elige tu primer arma")
            arma = input()
            sword2= setsword2(0)
            result = MONSTERS[12] + sword2[int(arma)]
            print("Elige tu segunda arma")
            arma =input()
            if int(arma)==6:
                resultado = godsword(MONSTERS[12])
                if resultado == 1:
                    print("Has acertado, prueba otros niveles")
                    niveles(nombre)
                else:
                    print("Has fallado, vuelve a intentarlo")
                    niveles(nombre)
            else:
                sword2 = setsword2(1)
                result = result + sword2[int(arma)]
                counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
                array = dic_to_array(counts)
                logicaqubit2(array,counts,nombre,result)
        if nivelInt==14:
            pass

def main():
    setWeapons()
    setMonsters()
    inicio()
    nombre=input()
    niveles(nombre)
if __name__ == '__main__':
    main()