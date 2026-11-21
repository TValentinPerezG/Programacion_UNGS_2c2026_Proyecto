from ... import configuracion
from ..utilidades import horas, listas, textos


def horariosEnAula(oferta, aula, dia):
    """Recibe la oferta, un aula (por ejemplo "7118") y un día (por ejemplo "viernes").
    Busca los horarios que se dictan en esa aula ese día, sin importar mayúsculas ni tildes.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: horariosEnAula(oferta, "7118", "viernes") devuelve los horarios de Análisis
    Numérico y de Introducción a la Programación."""
    horarios_materias = []
    for horario in oferta:
        if textos.extraerNumero(horario[configuracion.POSICION_AULA]) == textos.extraerNumero(aula) and textos.normalizar(horario[configuracion.POSICION_DIA]) == textos.normalizar(dia):
            horarios_materias.append(horario) 
    return horarios_materias


def ordenarPorHora(horarios):
    """Recibe una lista de horarios.
    Arma una copia ordenada por hora de inicio, de la más temprana a la más tarde, con el método
    de inserción (sin usar sorted). La lista que recibe no cambia.
    Devuelve la lista ordenada.
    Ejemplo: con un horario que empieza a las 18:00 y otro a las 13:00, devuelve primero el de las 13:00."""
    copia = listas.copiarLista(horarios)
    hora_en_minutos = []
    for hora in copia:
        hora_en_minutos.append(horas.horaAMinutos(hora[configuracion.POSICION_HORA_INICIO]))
    for posicion in range(len(hora_en_minutos)):
        actual = posicion
        while actual - 1 >= 0 and hora_en_minutos[actual-1] > hora_en_minutos[actual]:
            hora_en_minutos[actual - 1], hora_en_minutos[actual] = hora_en_minutos[actual], hora_en_minutos[actual - 1]
            copia[actual - 1], copia[actual] = copia[actual], copia[actual - 1]
            actual = actual - 1
    
    return copia
