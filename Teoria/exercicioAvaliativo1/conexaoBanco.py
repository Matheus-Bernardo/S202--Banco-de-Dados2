#conexaoBanco.py
from pymongo import MongoClient
import matplotlib.pyplot as plt
client = MongoClient('mongodb://localhost:27017')
db = client['bancoiot']
sensores = db.sensores

class Banco:
    def cadastrarTemperatura(self, temperatura, sensor):

        if(temperatura<=38):
            sensores.insert_one({
                "nomeSensor": sensor,
                "valorSensor": temperatura,
                "UnidadeMedida": "°C",
                "sensorAlarmado": "False"
            })
        else:
            sensores.insert_one({
                "nomeSensor": sensor,
                "valorSensor": temperatura,
                "UnidadeMedida": "°C",
                "sensorAlarmado": "true"
            })

    #desafio imposto
    def dadosTemperatura(self):
        dadosTemperatura = sensores.find()
        temperaturas = [dados['valorSensor'] for dados in dadosTemperatura]
        indices = list(range(1, len(temperaturas) + 1))

        # Plotar o gráfico
        plt.plot(indices, temperaturas, marker='o')
        plt.title('Temperaturas Registradas')
        plt.xlabel('Registros')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        plt.show()
