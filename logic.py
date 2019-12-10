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
    # qubits de 2
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
    MONSTERS.append(swaprandom)
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

def dic_to_array(dic):
    array=[]
    for key in dic.keys():
        array.append(key)

    return array


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
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

            if array[1] == '10':
                print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                porcentaje = counts['00']
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

            if array[1] == '11':
                print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                porcentaje = counts['00']
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

        if array[1]=="00":
            if array[0] == '01':
                print("El valor del '00' es:", counts['00'], ", el valor del '01' es: ", counts['01'])
                porcentaje = counts['00']
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

            if array[0] == '10':
                print("El valor del '00' es:", counts['00'], ", el valor del '10' es: ", counts['10'])
                porcentaje = counts['00']
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

            if array[0] == '11':
                print("El valor del '00' es:", counts['00'], ", el valor del '11' es: ", counts['11'])
                porcentaje = counts['00']
                print("El arma no ha sido el correcto,vamos a probar si has tenido suerte")
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1).result().get_counts()
            array = dic_to_array(counts)

    else:
        if array[0]=='00':
            pass



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

    print(diclist)
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

def qubit1function(level, weapon):
    result = MONSTERS[level] + WEAPONS[int(weapon)]
    return  result
def niveles(nombre, nivelInt):

    if nivelInt == 8:
        print("Has selecionado el 8º nivel")
        print(
            "Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
        print(MONSTERS[7].draw())
        print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")

        print("Elige tu primer arma")
        arma = input()
        if arma == 6:
            godsword(MONSTERS[7])
        else:
            sword2 = setsword2(0)
            result = MONSTERS[7] + sword2[int(arma)]
            print("Elige tu segunda arma")
            sword2 = setsword2(1)
            result = result + sword2[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit2(array, counts, nombre, result)
    if nivelInt == 9:
        if arma == 6:
            godsword(MONSTERS[8])
        else:
            arma = input()
            sword2 = setsword2(0)
            result = MONSTERS[8] + sword2[int(arma)]
            print("Elige tu segunda arma")
            arma = input()
            sword2 = setsword2(1)
            result = result + sword2[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit2(array, counts, nombre, result)
    if nivelInt == 10:
        print("Has selecionado el 10º nivel")
        print(
            "Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
        print(MONSTERS[9].draw())
        print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
        print("Elige tu primer arma")
        arma = input()
        if arma == 6:
            godsword(MONSTERS[9])
        else:
            sword2 = setsword2(0)
            result = MONSTERS[9] + sword2[int(arma)]
            print("Elige tu segunda arma")
            arma = input()
            sword2 = setsword2(1)
            result = result + sword2[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit2(array, counts, nombre, result)
    if nivelInt == 11:
        print("Has selecionado el 11º nivel")
        print(
            "Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
        print(MONSTERS[10].draw())
        print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
        print("Elige tu primer arma")
        arma = input()
        if arma == 6:
            godsword(MONSTERS[10])
        else:
            sword2 = setsword2(0)
            result = MONSTERS[10] + sword2[int(arma)]
            print("Elige tu segunda arma")
            arma = input()
            sword2 = setsword2(1)
            result = result + sword2[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit2(array, counts, nombre, result)
    if nivelInt == 12:
        print("Has selecionado el 12º nivel")
        print(
            "Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
        print(MONSTERS[11].draw())
        print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")
        print("Elige tu primer arma")
        arma = input()
        if arma == 6:
            godsword(MONSTERS[11])
        else:
            sword2 = setsword2(0)
            result = MONSTERS[11] + sword2[int(arma)]
            print("Elige tu segunda arma")
            arma = input()
            sword2 = setsword2(1)
            result = result + sword2[int(arma)]
            counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
            array = dic_to_array(counts)
            logicaqubit2(array, counts, nombre, result)
    if nivelInt == 13:
        print("Has selecionado el 13º nivel")
        print(
            "Estas en un nivel superior, en este caso tendras que atacar dos veces. En el primer caso atacaremos al qubit 0 y en el segundo atacaremos al qubit 1")
        print(MONSTERS[12].draw())
        print("Este es tu enemigo,intenta matarlo elegiendo el arma que veas optima. Eligiendolas del 0 al 5")

        print("Elige tu primer arma")
        arma = input()
        sword2 = setsword2(0)
        result = MONSTERS[12] + sword2[int(arma)]
        print("Elige tu segunda arma")
        arma = input()
        sword2 = setsword2(1)
        result = result + sword2[int(arma)]
        counts = execute(result, Aer.get_backend('qasm_simulator'), shots=1000).result().get_counts()
        array = dic_to_array(counts)
        logicaqubit2(array, counts, nombre, result)
    if nivelInt == 14:
        pass

def main():
    setWeapons()
    setMonsters()
    nombre=input()
    niveles(nombre)



if __name__ == '__main__':
    main()