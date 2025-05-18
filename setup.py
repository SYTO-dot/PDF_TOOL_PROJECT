# setup.py (for Windows EXE build)
from setuptools import setup

setup(
    name='SOLTECH_PDF_Tool',
    version='1.0',
    description='A simple offline PDF merge and split tool built with PyQt5 and PyPDF2',
    author='Engr. Saheed',
    author_email='your-email@example.com',
    packages=[],
    install_requires=[
        'PyQt5',
        'PyPDF2'
    ],
    entry_points={
        'gui_scripts': [
            'pdf_tool = main:main'
        ]
    },
)
