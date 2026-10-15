"""
Comprobaciones automaticas de la practica integradora de la UD0.

Se ejecutan en GitHub Actions tras cada push. Orientan durante el trabajo:
una comprobacion superada no garantiza la calificacion, que pone el profesorado.

Para ejecutarlas en el equipo (con el entorno virtual activado):
    pip install pytest nbformat
    python -m pytest -v tests
"""

import re
import subprocess
from pathlib import Path

import nbformat

RAIZ = Path(__file__).resolve().parent.parent
COMMITS_PROPIOS = 4  # sin contar el commit inicial que crea la plantilla


def git(*args):
    proceso = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)
    return proceso.stdout.strip()


def test_estructura_de_carpetas():
    for carpeta in ("datos", "notebooks", "src"):
        assert (RAIZ / carpeta).is_dir(), f"Falta la carpeta «{carpeta}»."


def test_carpeta_datos_versionada():
    assert (RAIZ / "datos" / ".gitkeep").is_file(), (
        "Git no versiona carpetas vacías: la carpeta «datos» necesita un archivo vacío «.gitkeep»."
    )


def test_readme():
    readme = RAIZ / "README.md"
    assert readme.is_file(), "Falta el archivo README.md."
    texto = readme.read_text(encoding="utf-8")
    assert re.search(r"^# \S", texto, re.MULTILINE), "El README.md no tiene un título de nivel 1."
    filas = [l for l in texto.splitlines() if l.strip().startswith("|") and "wikipedia.org" in l]
    assert len(filas) >= 4, (
        f"La tabla del README.md debe tener al menos cuatro figuras con enlace a Wikipedia; hay {len(filas)}."
    )
    assert re.search(r"^#+\s*puesta en marcha", texto, re.MULTILINE | re.IGNORECASE), (
        "Falta la sección «Puesta en marcha» en el README.md."
    )


def test_gitignore_excluye_el_entorno():
    gitignore = RAIZ / ".gitignore"
    assert gitignore.is_file(), "Falta el archivo .gitignore."
    assert ".venv" in gitignore.read_text(encoding="utf-8"), "El .gitignore no excluye el entorno virtual .venv."


def test_entorno_virtual_no_versionado():
    versionados = git("ls-files", ".venv")
    assert versionados == "", "El entorno virtual .venv está en el repositorio: se retira con git rm -r --cached .venv."


def test_requirements():
    requisitos = RAIZ / "requirements.txt"
    assert requisitos.is_file(), "Falta el archivo requirements.txt."
    datos = requisitos.read_bytes()

    # pip freeze > requirements.txt en Windows PowerShell 5.1 escribe UTF-16
    utf16 = datos.startswith((b"\xff\xfe", b"\xfe\xff")) or b"\x00" in datos
    assert not utf16, (
        "El requirements.txt está codificado en UTF-16, no en UTF-8: suele ocurrir al "
        "generarlo con 'pip freeze > requirements.txt' en Windows PowerShell. Se vuelve "
        "a generar con 'python -m pip freeze | Out-File -Encoding utf8 requirements.txt' "
        "(o desde cmd o Git Bash) y se sube de nuevo."
    )
    texto = datos.decode("utf-8-sig", errors="replace")
    assert "ipython" in texto.lower(), "El requirements.txt no incluye ipython."


def test_cuaderno():
    ruta = RAIZ / "notebooks" / "exploracion.ipynb"
    assert ruta.is_file(), "Falta el cuaderno notebooks/exploracion.ipynb."
    cuaderno = nbformat.read(ruta, as_version=4)
    nbformat.validate(cuaderno)
    tipos = {celda.cell_type for celda in cuaderno.cells}
    assert "markdown" in tipos, "El cuaderno no tiene ninguna celda de texto en Markdown."
    assert "code" in tipos, "El cuaderno no tiene ninguna celda de código."
    codigo = "\n".join(c.source for c in cuaderno.cells if c.cell_type == "code")
    assert "version" in codigo, "Ninguna celda de código muestra la versión de Python."


def test_script_principal():
    script = RAIZ / "src" / "principal.py"
    assert script.is_file(), "Falta el script src/principal.py."
    # compila sin ejecutar: detecta errores de sintaxis
    compile(script.read_text(encoding="utf-8"), str(script), "exec")


def test_historial():
    total = int(git("rev-list", "--count", "HEAD") or 0)
    propios = total - 1
    assert propios >= COMMITS_PROPIOS, (
        f"Se esperan al menos {COMMITS_PROPIOS} commits propios, repartidos a lo largo del trabajo; hay {propios}."
    )
