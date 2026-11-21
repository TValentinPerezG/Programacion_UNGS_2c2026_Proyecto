MINUTOS_POR_HORA = 60


def horaAMinutos(hora):
    """Recibe una hora escrita como "HH:MM".
    Calcula cuántos minutos pasaron desde las 00:00.
    Devuelve esa cantidad de minutos.
    Ejemplo: horaAMinutos("18:30") devuelve 1110."""
    total = 0
    minutos = hora[3] + hora[4]
    horas = hora[0] + hora[1]
    total = int(minutos) + MINUTOS_POR_HORA * int(horas)
    
    return total
