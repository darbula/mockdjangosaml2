import os
from setuptools import setup, find_packages


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mockdjangosaml2',
    version='0.16.0',
    url='http://github.com/darbula/mockdjangosaml2',
    author='Damir Arbula',
    author_email='damir.arbula@gmail.com',
    description='Django application that mocks functionality of djangosaml2 app for testing and development purposes.',
    license='BSD',
    platforms=['Windows', 'Linux', 'Mac OSX'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
    ],
    long_description=read('README.rst'),
)
