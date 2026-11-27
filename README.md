<p align="center"><b>Trabajo práctico de Introducción a la Programación · 2.º semestre 2026</b></p>



# Informe del Trabajo Práctico: SarmIA

> **Materia:** Introducción a la Programación — Universidad Nacional de General Sarmiento (UNGS)  
> **Semestre:** 2.º semestre 2026  
> **Integrantes:** Tobias Valentin Perez Gomez y Luca Lagraña Giménez

## 1. Introducción

SarmIA es un asistente conversacional pensado para ayudar a estudiantes de la UNGS a consultar información de la oferta académica de la cursada, como materias, comisiones, aulas y horarios.

A través de una conversación, permite buscar materias o comisiones, consultar qué horarios se dictan en un aula en determinado día, saber en qué turno empieza un horario y detectar si distintos horarios se superponen entre sí.

## 2. Funciones implementadas, dificultades y decisiones tomadas

### A. Módulo `sarmi/capas/servicios/superposiciones.py` (Luca Lagraña Giménez)

#### `seSuperponen(horarioA, horarioB)`

- **Explicación:** Revisa dos horarios (por ejemplo, de dos comisiones) y devuelve verdadero si se superponen o falso si no se superponen. Si alguno de los horarios es virtual o si son de distinto día, devuelve falso de entrada; si son del mismo día y no virtuales, pasa inicio y fin a minutos y devuelve falso solo cuando un rango termina antes o justo cuando empieza el otro.

- **Código:**

```python
def seSuperponen(horarioA, horarioB):
    diaA = horarioA[configuracion.POSICION_DIA]
    diaB = horarioB[configuracion.POSICION_DIA]

    if diaA == configuracion.DIA_VIRTUAL or diaB == configuracion.DIA_VIRTUAL:
        return False

    if diaA != diaB:
        return False

    inicioA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_INICIO])
    FinA = horas.horaAMinutos(horarioA[configuracion.POSICION_HORA_FIN])
    inicioB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_INICIO])
    finB = horas.horaAMinutos(horarioB[configuracion.POSICION_HORA_FIN])

    if finA <= inicioB or finB <= inicioA:
        return False

    return True
```

#### `buscarSuperposiciones(horariosA, horariosB)`

- **Explicación:** Compara cada horario de la primera lista con cada horario de la segunda y devuelve una lista con los pares `[horarioA, horarioB]` que chocan, o una lista vacía si no hay ninguno.

- **Código:**

```python
def buscarSuperposiciones(horariosA, horariosB):
    superposiciones = []

    for horarioA in horariosA:
        for horarioB in horariosB:
            if seSuperponen(horarioA, horarioB):
                superposiciones.append([horarioA, horarioB])

    return superposiciones
```

#### Dificultades y decisiones tomadas

- Al principio la mayor dificultad fue ubicarme en la organización general del proyecto, identificar dónde estaban definidas las posiciones de cada campo y manejar el flujo de trabajo con Git y GitHub.
- Se decidió descartar primero los casos de horarios virtuales (`DIA_VIRTUAL`) y de días distintos (`diaA != diaB`) para no evaluar horas cuando no puede haber superposición.
- Para los horarios presenciales del mismo día, se decidió pasar inicio y fin a minutos y usar `<=` (`finA <= inicioB or finB <= inicioA`) para que si un horario empieza justo cuando termina el otro no cuente como superposición. También se reutilizó `seSuperponen` dentro de `buscarSuperposiciones` para no repetir la comparación.

---

### B. Módulos implementados por Tobias Valentin Perez Gomez

#### 1. `sarmi/capas/utilidades/listas.py`

##### `esta(elemento, lista)`

- **Explicación:** Indica si `elemento` aparece en `lista` devolviendo verdadero o falso.

##### `copiarLista(lista)`

- **Explicación:** Crea y devuelve una lista nueva con los mismos elementos en el mismo orden, sin modificar la lista original.

- **Código:**

```python
def esta(elemento, lista):
    for elem in lista:
        if elem == elemento:
            return True

    return False


def copiarLista(lista):
    nueva = []

    for elem in lista:
        nueva.append(elem)

    return nueva
```

#### 2. `sarmi/capas/utilidades/textos.py`

##### `normalizar(texto)`

- **Explicación:** Convierte texto a minúsculas y reemplaza las letras con tilde por su equivalente sin tilde según la configuración.

##### `contiene(texto, buscado)`

- **Explicación:** Normaliza `texto` y verifica si `buscado` aparece dentro de él.

- **Código:**

```python
def normalizar(texto):
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
    texto_normalizado = normalizar(texto)

    return buscado in texto_normalizado
```

#### 3. `sarmi/capas/utilidades/horas.py`

##### `horaAMinutos(hora)`

- **Explicación:** Recibe una hora en formato `"HH:MM"` y calcula cuántos minutos pasaron desde las 00:00. Se tiene una condicion si por cualquier motivo se recibe mal el dato, y se utiliza una constante del largo de la hora.

- **Código:**

```python
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
```

#### 4. `sarmi/capas/servicios/materias.py`

##### `valoresDistintos(horarios, posicion)`

- **Explicación:** Recorre los horarios y reúne los valores ubicados en `posicion` sin repetir, evitando duplicados con la función `esta`.

##### `buscarMateria(oferta, nombre)`

- **Explicación:** Busca en `oferta` los horarios cuya materia contiene `nombre`, normalizando mayúsculas y tildes.

##### `filtrarMateriaExacta(horarios, nombre)`

- **Explicación:** Filtra la lista quedándose solo con los horarios cuyo nombre de materia coincide exactamente (normalizado) con `nombre`.

##### `filtrarPorComision(horarios, comision)`

- **Explicación:** Extrae el número de comisión y devuelve los horarios que pertenecen a esa comisión.

- **Código:**

```python
def valoresDistintos(horarios, posicion):
    distintos = []

    for elem in horarios:
        if not listas.esta(elem[posicion], distintos):
            distintos.append(elem[posicion])

    return distintos


def buscarMateria(oferta, nombre):
    horarios_materia = []

    for materia in oferta:
        if textos.contiene(textos.normalizar(materia[configuracion.POSICION_MATERIA]), textos.normalizar(nombre)):
            horarios_materia.append(materia)

    return horarios_materia


def filtrarMateriaExacta(horarios, nombre):
    horarios_materia = []

    for materia in horarios:
        if textos.normalizar(materia[configuracion.POSICION_MATERIA]) == textos.normalizar(nombre):
            horarios_materia.append(materia)

    return horarios_materia


def filtrarPorComision(horarios, comision):
    com = textos.extraerNumero(comision)
    horarios_comision = []

    for materia in horarios:
        if textos.extraerNumero(materia[configuracion.POSICION_COMISION]) == com:
            horarios_comision.append(materia)

    return horarios_comision
```

#### 5. `sarmi/capas/servicios/aulas.py`

##### `horariosEnAula(oferta, aula, dia)`

- **Explicación:** Devuelve los horarios de `oferta` que corresponden al aula y al día solicitados.

##### `ordenarPorHora(horarios)`

- **Explicación:** Arma y devuelve una copia ordenada de menor a mayor según la hora de inicio en minutos, sin modificar la lista original.

- **Código:**

```python
def horariosEnAula(oferta, aula, dia):
    horarios_materias = []

    for horario in oferta:
        if textos.extraerNumero(horario[configuracion.POSICION_AULA]) == textos.extraerNumero(aula) and textos.normalizar(horario[configuracion.POSICION_DIA]) == textos.normalizar(dia):
            horarios_materias.append(horario)

    return horarios_materias


def ordenarPorHora(horarios):
    copia = listas.copiarLista(horarios)
    hora_en_minutos = []

    for hora in copia:
        hora_en_minutos.append(horas.horaAMinutos(hora[configuracion.POSICION_HORA_INICIO]))

    for posicion in range(len(hora_en_minutos)):
        actual = posicion

        while actual - 1 >= 0 and hora_en_minutos[actual - 1] > hora_en_minutos[actual]:
            hora_en_minutos[actual - 1], hora_en_minutos[actual] = hora_en_minutos[actual], hora_en_minutos[actual - 1]
            copia[actual - 1], copia[actual] = copia[actual], copia[actual - 1]
            actual = actual - 1

    return copia
```

#### 6. `sarmi/capas/servicios/turnos.py` (Opcional)

##### `turnoDe(horario)`

- **Explicación:** Determina si el horario empieza en el turno `"mañana"`, `"tarde"` o `"noche"` según los rangos configurados, o devuelve `""` si no corresponde a ninguno.

##### `filtrarPorTurno(horarios, turno)`

- **Explicación:** Filtra la lista y devuelve los horarios cuyo turno inicial coincide con `turno`. La condicion al inicio evita casos donde se rompa las comparaciones por un horario sin hora de inicio.

- **Código:**

```python
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
    horarios_turno = []

    for horario in horarios:
        inicio = turnoDe(horario)

        if textos.normalizar(inicio) == textos.normalizar(turno):
            horarios_turno.append(horario)

    return horarios_turno
```

##### Dificultades y decisiones tomadas

- 

---

## 3. Uso de IA

Se utilizó asistencia de IA como apoyo para comprender la consigna y la estructura del proyecto, revisar casos y lógicas de las funciones, y redactar y organizar este informe.

Se adaptaron las implementaciones a las constantes, funciones auxiliares y criterios del proyecto —reutilizando utilidades propias y comprobando con los tests— y se revisó el documento para ajustarlo a lo pedido.

