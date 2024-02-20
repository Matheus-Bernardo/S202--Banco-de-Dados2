class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self,assunto):
        print("O professor " + self.nome + " está ministrando uma aula sobre o assunto: "+assunto)

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print("O aluno " +self.nome + " esta presente")


class Aula:
    def __init__(self, professor: Professor, assunto):
     self._professor = professor
     self.assunto = assunto
     self.alunos = []

    def adicionarAluno(self,aluno : Aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print("Presença na aula sobre " + self.assunto + ", ministrada pelo "     
                                                         "professor " + professor.nome)
        for i in self.alunos:
            i.presenca()



professor = Professor('Bruninho')
aluno1 = Aluno('Matheus')
aluno2 = Aluno('Eliana')
aula = Aula(professor,'redes neurais')
aula.adicionarAluno(aluno1)
aula.adicionarAluno(aluno2)

aula.listar_presenca()