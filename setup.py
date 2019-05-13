from setuptools import setup, find_packages


requirements = [
    'tensorflow',
    'hypergan',
    'hyperchamber',
    'numpy',
    'pillow',
    'pygame',
    'keras',
    'tqdm',
    'autokeras',
]


setup(
    name='moon',
    version='0.1',
    description='moon board climb generation and grading',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True
)
