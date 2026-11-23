<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="imagenes/sarmia-oscuro.png">
    <img src="imagenes/sarmia.png" alt="SarmIA, el agente de la UNGS" width="460">
  </picture>
</p>

<p align="center"><b>Trabajo práctico de Introducción a la Programación · 2.º semestre 2026</b></p>


- **Persistencia** (lee la oferta académica del archivo CSV).
- **Utilidades** (funciones generales sobre listas, textos y horas, que se reutilizan en todo el proyecto).
- **Servicios** (la lógica del problema: buscar materias, aulas, superposiciones y turnos, y armar las respuestas).
- **Herramientas** (las funciones que el modelo puede usar; solo llaman a los servicios).
- **Controles** (revisan la pregunta antes de que llegue al modelo).

```
sarmi/
├── agent.py                  Define el agente: modelo, instrucciones y herramientas
├── configuracion.py          Valores configurables
├── datos/oferta.csv          Oferta académica (un horario por fila)
└── capas/
    ├── persistencia/         repositorio.py
    ├── utilidades/           listas.py, textos.py, horas.py
    ├── servicios/            materias.py, aulas.py, superposiciones.py, turnos.py, consultas.py
    ├── herramientas/         herramientas.py
    └── controles/            controles.py
tests/                        Tests de las funciones
configurarClave.py            Guarda la clave de Gemini
verificarEntorno.py           Revisa que la instalación esté completa
```


### 📝 Formato de entrega
- La entrega se divide en 2 partes: **código** e **informe**:

  - **Parte 1: código:** todo el desarrollo debe estar en un repositorio interno del grupo (*fork* del repo base del TP). Se debe agregar a los docentes de la comisión para que puedan seguir los avances (corregir funciones, dar sugerencias, etc.). Dado el caudal de alumnos, **los estudiantes son responsables de avisar a los docentes para revisar una pre-entrega o resolver cualquier duda que bloquee el avance del TP**.

    Sugerimos:
      - Que cada integrante tenga su propia cuenta de GitHub, NO usar una única en el proyecto.
      - Cada integrante debe *commitear* una o varias porciones de código, dependiendo cómo distribuyan el trabajo. **Se debe visualizar el aporte individual al TP.**
      - **Nunca subir el archivo ```.env``` con la clave.**

  - **Parte 2: informe:** deben redactar un documento donde exista una introducción que explique de qué se trata el trabajo (sin utilizar lenguaje técnico), que incluya el código de las funciones implementadas y una breve explicación de cada una de ellas junto con las **dificultades de implementación** y **decisiones tomadas** -con su correspondiente justificación-. **NO incluir explicaciones de funcionalidades de Python, ADK o similares**. Si usaron IA para programar, contar para qué la usaron y qué cambiaron de lo que propuso. Este documento debe estar en formato PDF anexo dentro de la carpeta del TP.

  🔥 **Se DEBE cumplir con ambas partes (código + informe) para aprobar el trabajo práctico.**

### 📝 Documentación adicional
- Documentación oficial de Google ADK disponible aquí: https://google.github.io/adk-docs/
- Cómo crear la clave de Gemini: https://ai.google.dev/gemini-api/docs/api-key
- Sección **GIT**
    - Introducción a GIT: [clic acá](https://www.youtube.com/watch?v=mzHWafbVRyU).
    - Manejo de ramas/branches: [clic acá](https://www.youtube.com/watch?v=BRY9gamL9PE).
    - Merge & resolución de conflictos: [clic acá](https://www.youtube.com/watch?v=9YUaf-uxuRM).
