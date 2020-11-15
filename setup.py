from setuptools import setup, find_packages

setup(
    name='snakegame',
    url='https://github.com/ChiaraCampagnola/python-snake',
    author='Chiara Campagnola',
    author_email='chiaracampagnola@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['play-snake=snakegame.main:main']
    },
    version='0.1',
    license='MIT',
    description='Simple snake game',
)