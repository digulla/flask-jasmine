"""
Flask-Jasmine
-------------

This is extension to execute BDD tests with Jasmine BDD Framework.
Also extension support for Bundles created by ``Flask-Assets``.
"""

from setuptools import setup


setup(
    name='Flask-Jasmine',
    version='2.0',
    url='https://github.com/joymax/flask-jasmine',
    license='BSD',
    author='Aaron Digulla',
    author_email='digulla@hepe.com',
    description='Execution of Jasmine JavaScript tests within Flask. Based on the work of Maksym Klymyshyn <klymyshyn@gmail.com>',
    long_description=__doc__,
    packages=['flask_jasmine'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
