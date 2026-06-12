from setuptools import setup, find_packages

setup(
    name='axentx-product',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest'],
    package_data={'': ['*']},
    include_package_data=True,
)
