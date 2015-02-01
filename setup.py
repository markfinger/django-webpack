from setuptools import setup

VERSION = '2.1.1'

setup(
    name='django-webpack',
    version=VERSION,
    packages=['django_webpack'],
    package_data={
        'django_webpack': [
            'bundle.js',
            'package.json',
        ]
    },
    install_requires=[
        'django',
        'django-node==2.3.2',
    ],
    description='Generate Webpack bundles from a Django application.',
    long_description='Documentation at https://github.com/markfinger/django-webpack',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/django-webpack',
)