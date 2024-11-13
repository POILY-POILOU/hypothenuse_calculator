from setuptools import setup, find_packages

setup(
    name="hypotenuse_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    tests_require=["pytest", "coverage"],
    entry_points={
        'console_scripts': [
            'calculate-hypotenuse=hypotenuse.calculator:calculate_hypotenuse',
        ],
    },
)
