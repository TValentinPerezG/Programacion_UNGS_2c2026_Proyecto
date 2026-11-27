from ... import configuracion
from ..utilidades import horas, textos


def turnoDe(horario):
    """OPCIONAL. Recibe un horario.
    Se fija en qué turno empieza, según TURNOS en configuracion.py.
    Devuelve "mañana", "tarde" o "noche", o "" si el horario es virtual.
    Ejemplo: un horario que empieza a las 18:00 devuelve "noche"."""
    
    if horario[configuracion.POSICION_HORA_INICIO] == "":
        return ""
    
    hora_inicio_minutos = horas.horaAMinutos(horario[configuracion.POSICION_HORA_INICIO])
    
    if horas.horaAMinutos(configuracion.TURNOS[0][2]) > hora_inicio_minutos >= horas.horaAMinutos(configuracion.TURNOS[0][1]):
        return "mañana"
    
    elif horas.horaAMinutos(configuracion.TURNOS[1][2]) > hora_inicio_minutos >= horas.horaAMinutos(configuracion.TURNOS[1][1]):
        return "tarde"
        
    elif horas.horaAMinutos(configuracion.TURNOS[2][2]) >= hora_inicio_minutos >= horas.horaAMinutos(configuracion.TURNOS[2][1]):
        return "noche"
    
    
    return ""


def filtrarPorTurno(horarios, turno):
    """OPCIONAL. Recibe una lista de horarios y un turno ("mañana", "tarde" o "noche").
    Se queda con los horarios que empiezan en ese turno.
    Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
    Ejemplo: con los horarios de Álgebra I y "noche", devuelve el de la COM-02 
    (miércoles 18:00)."""
    horarios_turno = []
    
    for horario in horarios:
        inicio = turnoDe(horario)
        if textos.normalizar(inicio) == textos.normalizar(turno):
            horarios_turno.append(horario)
             
    return horarios_turno
