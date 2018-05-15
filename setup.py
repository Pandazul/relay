from setuptools import setup, find_packages

setup(
    name='imaprelay',
    description='IMAP Round Robin',
    long_description=long_description,
    author='',
    author_email='',
    url='',
    license='OPENSOURCE',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
rs={
        'console_scripts': [
            'imaprelay = imaprelay.command:main'
        ]
    }
)