from setuptools import setup, find_packages

setup(
    name='flask-waf',
    version='1.0.0',
    packages=find_packages(),
    author='Ishan Oshada',
    author_email='ic31908@gmail.com',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/Flask-Waf',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        
        "lask","Werkzeug","itsdangerous","click","PyYAML","jsonschema","requests","cryptography","python-dotenv"
    ],
)
