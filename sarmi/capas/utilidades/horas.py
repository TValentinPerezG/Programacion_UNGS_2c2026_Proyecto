MINUTOS_POR_HORA = 60


def horaAMinutos(hora):
    """Recibe una hora escrita como "HH:MM".
    Calcula cuántos minutos pasaron desde las 00:00.
    Devuelve esa cantidad de minutos.
    Ejemplo: horaAMinutos("18:30") devuelve 1110."""
    total = 0
    hrsYMin = hora.split(":")
    
    # Para cuando solo se reciben las horas
    if len(hrsYMin) == 1:
        return hrsYMin[0] * MINUTOS_POR_HORA    
    
    total = int(hrsYMin[1]) + MINUTOS_POR_HORA * int(hrsYMin[0])
    
    return total
