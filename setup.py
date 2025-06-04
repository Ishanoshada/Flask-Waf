from setuptools import setup, find_packages

setup(
    name='flask_waf',
    version='2.1.0',
    packages=find_packages(),
    author='Ishan Oshada',
    author_email='ic31908@gmail.com',
    description='Flask-WAF is an advanced Web Application Firewall (WAF) extension for Flask applications. It provides comprehensive protection against various web application threats, enhancing the security of your Flask-based web applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/Flask-Waf',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
