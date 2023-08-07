from setuptools import setup

setup(
    name='nyseconverter',
    version='0.1',
    description='NYSE Converter',
    url='https://github.com/avijayal/nyse-converter',
    author='avijayal',
    author_email='3002.vijayalakshmi@gmail.com',
    license='MIT',
    packages=['nyseconverter'],
    install_requires=['dask[complete]<=2023.7.1'],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['nc=nyseconverter:main'],
    }
)