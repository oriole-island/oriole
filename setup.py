import sys

from setuptools import find_packages, setup

if sys.version_info[:2] < (3, 6):
    raise RuntimeError('Error: Python < 3.6')

install_requires = [
    "pyyaml==5.1",
    "pyetcd==1.8.0",
    "SQLAlchemy==1.2.14",
    "mogo==0.4.0",
    "redis==2.10.6",
    "Babel==2.5.3",
    "Jinja2==2.10",
    "PyMySQL==0.7.11",
    "mysqlclient==1.3.12",
    "pytest==3.2.3",
    "Sphinx==1.7.2",
    "mockredispy==2.9.3",
    "mongomock==3.8.0",
]

setup(
    name='oriole',
    version='16.1.0',
    description='Oriole virtual system.',
    long_description=open('README.rst').read(),
    author='Eric.Zhou',
    author_email='xiaoxiang.cn@gmail.com',
    url='https://github.com/oriole-island/oriole',
    packages=[],
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ])
