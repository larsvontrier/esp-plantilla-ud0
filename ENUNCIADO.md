# UD0. Práctica integradora: mujeres en la ciencia y en la música

Módulo 5098. Entornos y sintaxis en Python.

Este repositorio procede de la plantilla de la tarea. El archivo `ENUNCIADO.md` y las carpetas `.github` y `tests` forman parte de la plantilla y no se modifican.

---

## Antes de empezar

1. Comprobar que este repositorio es **privado** y que está en la cuenta personal, con el nombre `5098-ud0-usuario` (donde `usuario` es el nombre de la cuenta de GitHub).
2. Invitar como colaboradora a la cuenta del profesorado indicada en el aula virtual: **Settings**, **Collaborators**, **Add people**.
3. Clonar el repositorio en el equipo y trabajar siempre dentro de la carpeta clonada.

---

## Enunciado

Montar el entorno de trabajo del curso y documentar un mini-proyecto temático titulado **Mujeres en la ciencia y en la música**.

Contenido del repositorio:

- Estructura de carpetas con `datos`, `notebooks` y `src`. Git no versiona carpetas vacías, así que la carpeta `datos` lleva un archivo vacío llamado `.gitkeep`.
- Un entorno virtual `.venv` con `ipython` instalado y un `requirements.txt` generado, sin que el entorno llegue al repositorio.
- Un `README.md` en Markdown con: título, descripción del proyecto, una tabla de al menos cuatro figuras (nombre, campo y enlace a Wikipedia) y una sección de puesta en marcha.
- Un cuaderno `notebooks/exploracion.ipynb` con una celda de texto que presente el proyecto y una celda de código que muestre la versión de Python.
- Un script `src/principal.py` que muestre el título del proyecto.
- Un archivo `.gitignore` adecuado para un proyecto de Python con cuadernos.

Historial:

- Al menos cuatro commits propios, repartidos a lo largo del trabajo y con mensajes descriptivos que permitan seguir el proceso. Un único commit final no se considera válido.

---

## Comprobaciones automáticas

Tras cada `git push`, GitHub Actions ejecuta las comprobaciones de la carpeta `tests`. El resultado aparece junto a cada commit en la página del repositorio: marca verde si se superan todas y cruz roja si alguna falla. La pestaña **Actions** indica cuál y por qué.

Las comprobaciones orientan, pero no califican. También pueden ejecutarse en el equipo, con el entorno virtual activado:

```bash
pip install pytest nbformat
python -m pytest -v tests
```

---

## Entrega

1. Enviar todo el trabajo con `git push` y comprobar con `git status` que la rama está al día con `origin/main`.
2. Abrir la página del repositorio en GitHub y copiar el hash abreviado del último commit (siete caracteres). Si aparece en GitHub, está enviado.
3. Entregar en la tarea del aula virtual, antes de la fecha de cierre, un texto con estas dos líneas:

```text
Repositorio: https://github.com/usuario/5098-ud0-usuario
Commit: a1b2c3d
```

La versión corregida es la del commit indicado, aunque después se añadan otros. Si el plazo sigue abierto, la entrega se puede actualizar con un hash nuevo.
