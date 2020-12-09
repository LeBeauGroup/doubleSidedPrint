from setuptools import setup, find_packages
import os

# def package_files(directory):
#     paths = []
#     for (path, directories, filenames) in os.walk(directory):
#         for filename in filenames:
#             paths.append(os.path.join('..', path, filename))
#     return paths


setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='doubleSidedPrint',
    url='https://github.com/LeBeauGroup/doubleSidedPrint',
    author='James LeBeau',
    author_email='lebeau@mit.edu',
    # Needed to actually package something
    packages=find_packages(),
    entry_points ={
        'console_scripts': [
            'doubleSidePrint = doubleSidePrint.print:main'
        ]
    },

    # Needed for dependencies
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='GPLv3',
    description='Automatic double sided printing for all items in folder',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),


)
