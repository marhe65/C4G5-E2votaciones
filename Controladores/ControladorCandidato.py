from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
from Modelos.Candidato import Candidato
from Modelos.Resultado import Resultado
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict_

    def update(self, id, infoCandidato):
        candidatoActual=Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.numero = infoCandidato["Numero de resolución"]
        candidatoActual.cedula = infoCandidato["Cedula"]
        candidatoActual.nombre = infoCandidato["Nombre"]
        candidatoActual.apellido = infoCandidato["Apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)
    """"
    Relación entre Candidato y Partido
    """
    def asignarPartido(self,id,id_partido):
        candidatoActual=Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)

    """"
    Relación entre Candidato y Resultado
    """
    def asignarResultado(self, id, id_resultado):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        resultadoActual = Resultado(self.repositorioResultado.findById(id_resultado))
        candidatoActual.resultado = resultadoActual
        return self.repositorioCandidato.save(candidatoActual)