from Modelos.Partido import Partido
from Modelos.Resultado import Resultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioResultado = RepositorioResultado()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict_

    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero de resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
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