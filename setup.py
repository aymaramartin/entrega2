from setuptools import setup, find_packages   

setup(
    name='ModeloClientes',
    version='1.0',
    packages=find_packages(),
    install_requires=[],  # Aquí puedes agregar dependencias si las hay
    entry_points={
        'console_scripts': [
            'modelo-clientes = main:main',  # Hace que se pueda ejecutar main.py desde la terminal
        ],
    },
)

