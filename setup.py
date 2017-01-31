from setuptools import setup
from dataflow import __version__
__version__ = list(map(str, __version__))
setup(name='dataflow',
        version='.'.join(__version__),
        description='A dataflow diagram based sklearn interface',
        url='http://github.com/theSage21/dataflow',
        author='Arjoonn Sharma',
        author_email='arjoonn.94@gmail.com',
        license='MIT',
        packages=['dataflow'],
        entry_points = {
            'console_scripts': ['dataflow=dataflow.cli:main'],
            },
        install_requires=['bottle'],
        zip_safe=False)
