# Proyecto Base de Python

Este es un proyecto base de Python configurado con herramientas modernas de desarrollo.

## Características

- Gestión de dependencias con Pipenv
- Tipado estático con MyPy
- Formateo de código con Black
- Linting con Ruff
- Jupyter Notebooks configurados
- Pre-commit hooks para asegurar calidad de código

## Requisitos previos

- Python 3.10 o superior
- Pipenv
- Anaconda (opcional, pero recomendado para gestión de entornos)

## Instalación

### Usando Anaconda

1. Instala Anaconda desde [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

2. Crea un entorno conda:

   ```bash
   conda create -n proyecto-python python=3.10
   conda activate proyecto-python
   ```

3. Instala pipenv:

   ```bash
   conda install -c conda-forge pipenv
   ```

4. Instala las dependencias del proyecto:
   ```bash
   pipenv install --dev
   ```

### Sin Anaconda

1. Asegúrate de tener Python 3.10+ instalado:

   ```bash
   python --version
   ```

2. Instala pipenv:

   ```bash
   pip install pipenv
   ```

3. Instala las dependencias del proyecto:

   ```bash
   # Instalar dependencias principales
   conda install numpy pandas matplotlib scikit-learn

   # Instalar herramientas de desarrollo
   conda install black pytest
   conda install -c conda-forge mypy ruff pre-commit jupyter

   # Para paquetes no disponibles en conda
   pip install paquete-especial
   ```

4. Exportar el entorno para compartir:

   ```bash
   conda env export > environment.yml
   ```

5. Para recrear el entorno en otro sistema:

   ```bash
   conda env create -f environment.yml
   ```

   ```

   ```

## Configuración del entorno de desarrollo

1. Activa el entorno virtual:

   ```bash
   conda activate proyecto-python
   ```

2. Configura los pre-commit hooks:
   ```bash
   pre-commit install
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
