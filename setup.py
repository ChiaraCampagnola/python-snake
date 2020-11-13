from setuptools import setup

setup(
    name='Snake',
    url='https://github.com/ChiaraCampagnola/python-snake',
    author='Chiara Campagnola',
    author_email='chiaracampagnola@gmail.com',
    packages=['snake'],
    install_requires=['turtle'],
    entry_points={
        'console_scripts': ['play-snake=snake-game.main:main']
    },
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
)