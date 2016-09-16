import setuptools

setuptools.setup(
    name='payments',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=[
        'Flask==0.10.1',
        'gunicorn==19.4.5',
    ],
)
