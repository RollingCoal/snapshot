from setuptools import setup

setup(
    name='snapshotalyzer=3000',
    version='0.1',
    author='john dow',
    author_email="somthing@gmail.com",
    description="Snapshot something something",
    license="GPLv3+",
    packages=['shotty'],
    url="http://sdlkfjapoin.com",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
