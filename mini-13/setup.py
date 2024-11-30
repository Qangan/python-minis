from setuptools import setup, Extension

setup(
    name='matrix_power',
    version='1.3.3.7',
    description='Matrix mulptiple and power',
    ext_modules=[
        Extension(
            'matrix_power', 
            sources=['matrix_power.c']
            )
    ],
)
