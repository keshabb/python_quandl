from setuptools import setup, find_packages
setup(
    name = 'python_quandl',
    description = 'Python script to get stock info from quandl',
    version = '1.0',
    py_modules = ['stock'],
    author = 'Keshab Budhathoky',
    author_email = 'kb4it.professional@hotmail.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = [
        'click',
        'requests',
        'pandas',
        ],
    entry_points = {
        'console_scripts': [
        ]
    },
)
