# Proyecto Base de Python

Este es un proyecto base de Python configurado con herramientas modernas de desarrollo.

## Características

- Gestión de dependencias con Conda
- Tipado estático con MyPy
- Formateo de código con Black
- Linting con Ruff
- Jupyter Notebooks configurados
- Pre-commit hooks para asegurar calidad de código

## Requisitos previos

- Anaconda o Miniconda ([https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution))

## Configuración inicial del proyecto

1. Modifica el archivo `environment.yml` con el nombre de tu proyecto:

   ```yaml
   name: nombre-de-tu-proyecto # Cambia esto
   channels:
     - conda-forge
     - defaults
   dependencies:
     - python=3.10
     # Añade aquí tus dependencias
   ```

2. Crea el entorno virtual con las dependencias:

   ```bash
   conda env create -f environment.yml
   ```

3. Activa el entorno virtual:

   ```bash
   conda activate nombre-de-tu-proyecto
   ```

4. Configura los pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Uso diario del proyecto

1. Activa el entorno virtual:

   ```bash
   conda activate nombre-de-tu-proyecto
   ```

2. Para desactivar el entorno cuando termines:
   ```bash
   conda deactivate
   ```

## Ejecutar el proyecto

### Código Python

```bash
python src/main.py
```

### Jupyter Notebooks

```bash
jupyter notebook
```

## Estructura de directorios

```bash
proyecto-python/
├── src/
│ ├── __init__.py
│ ├── main.py
├── notebooks/
├── environment.yml
└── README.md
```

## Herramientas de desarrollo

- [Black](https://github.com/psf/black) - Formateador de código
- [Ruff](https://github.com/astral-sh/ruff) - Linter y formateador
- [Mypy](https://github.com/pre-commit/mirrors-mypy) - Tipado estático
- [Jupyter Notebook](https://jupyter.org/) - Entorno de desarrollo interactivo

## Gestión de dependencias

Si necesitas añadir nuevas dependencias al proyecto:

1. Instala el paquete con conda:

   ```bash
   conda install nombre_paquete
   ```

2. Actualiza el archivo environment.yml:

   ```bash
   conda env export --from-history > environment.yml
   ```
