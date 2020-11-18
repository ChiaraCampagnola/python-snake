from setuptools import setup, find_packages

setup(
    name='snakegame',
    url='https://github.com/ChiaraCampagnola/python-snake',
    author='Chiara Campagnola',
    author_email='chiaracampagnola@gmail.com',
    packages=find_packages(),
    package_data={'snakegame': ['resources/*.txt']},
    entry_points={
        'console_scripts': ['snakegame=snakegame.main:main']
    },
    version='0.1',
    python_requires='>=3.9',
    license='MIT',
    description='Simple snake game',
)
