from ... import configuracion


def normalizar(texto):
    """Recibe un texto.
    Lo pasa a minúsculas y le saca las tildes (ver LETRAS_CON_TILDE en configuracion.py).
    Devuelve el texto nuevo.
    Ejemplo: normalizar("Introducción a la PROGRAMACIÓN") devuelve "introduccion a la programacion"."""
    texto_normalizado = ""
    for caracter in texto:
        if caracter.lower() not in configuracion.LETRAS_CON_TILDE:
            texto_normalizado = texto_normalizado + caracter.lower()
        else: 
            for i in range(len(configuracion.LETRAS_CON_TILDE)):
                if caracter.lower() == configuracion.LETRAS_CON_TILDE[i]:
                    texto_normalizado = texto_normalizado + configuracion.LETRAS_SIN_TILDE[i]
                    break    
    
    return texto_normalizado


def contiene(texto, buscado):
    """Recibe dos textos: texto y buscado.
    Se fija si buscado aparece en alguna parte de texto.
    Devuelve True si aparece y False si no.
    Ejemplo: contiene("introduccion a la programacion", "program") devuelve True."""
    texto_normalizado = normalizar(texto)
    buscado_normalizado = normalizar(buscado)
    
    return buscado_normalizado.lower() in texto_normalizado.lower()


def extraerNumero(texto):
    """Recibe un texto.
    Junta los dígitos que aparecen en el texto y los convierte en número.
    Devuelve ese número, o -1 si el texto no tiene dígitos.
    Ejemplo: extraerNumero("COM-07") devuelve 7."""
    extraidos = ""
    numeros = "1234567890"
    for caracter in texto:
        if caracter in numeros:
            extraidos = extraidos + caracter
    if len(extraidos) > 0:
        return int(extraidos)    
        
    return -1
