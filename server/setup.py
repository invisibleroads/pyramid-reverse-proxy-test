from setuptools import setup, find_packages


setup(
    name='xyz',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'plaster_pastedeploy',
        'pyramid',
        'waitress',
    ],
    entry_points={
        'paste.app_factory': [
            'main = xyz:main',
        ],
    },
)
