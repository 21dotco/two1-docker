import setuptools

setuptools.setup(
    name='ping',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=[
        "docopt==0.6.2",
        "Flask==0.10.1",
        "geocoder==1.9.0",
        "gunicorn==19.4.5",
        "psutil==4.1.0",
        "PyYAML==3.11",
        "requests==2.7.0",
    ],
)
