from setuptools import setup

setup(
    name='micalculadora',
    version='0.1',
    description='Una librería para operaciones con tensores PyTorch',
    author='David Sanz',
    author_email='9001103@alumnos.ufv.es',
    url='https://github.com/02daviidd/RepositorioDavidSanz',
    packages=['micalculadora'],
    install_requires=[
        'torch',  # Añade aquí las dependencias de tu librería si las tienes
    ],
)