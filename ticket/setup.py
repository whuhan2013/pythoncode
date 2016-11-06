from setuptools import setup

setup(
    name='ticket',
    py_modules=['ticket', 'stations'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['ticket=ticket:cli']
    }
)