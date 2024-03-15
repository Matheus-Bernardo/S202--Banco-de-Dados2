import threading
import time
import random
from conexaoBanco import Banco

conect = Banco()

class SensorThread(threading.Thread):
    def __init__(self, nome, intervalo):
        threading.Thread.__init__(self)
        self.nome = nome
        self.intervalo = intervalo
        self.alarmado = False  # Variável para indicar se o sensor está alarmado

    def run(self):
        while not self.alarmado:  # Continua executando enquanto não estiver alarmado
            temp = gerar_numero_aleatorio()
            print(self.nome, "temperatura:", temp)
            conect.cadastrarTemperatura(temp, self.nome)
            if temp > 38:
                self.alarmado = True
                print("Atenção! Temperatura muito alta! Verificar", self.nome)
            time.sleep(self.intervalo)

def gerar_numero_aleatorio():
    return random.randint(30, 40)

# Criação das Threads
th1 = SensorThread('sensor1', 2)
th2 = SensorThread('sensor2', 3)
th3 = SensorThread('sensor3', 4)

# Inicia as Threads
th1.start()
th2.start()
th3.start()
# Aguarda as Threads terminarem
th1.join()
th2.join()
th3.join()

conect.dadosTemperatura()
