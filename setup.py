"""Setup file for handling packaging and distribution."""
from setuptools import setup

__version__ = "1.0.0"

setup(
    name="recursive_decorator",
    version=__version__,
    description="",
    license="MIT",
    author="ronen-y",
    email="ronenya4321@gmail.com",
    url="https://github.com/ronen-y/recursive_decorator",
    keywords="decorator recursive recursive_decorator recursive-decorator",
    install_requires=["codetransformer"],
    packages=["recursive_decorator"],
    extras_require={
            'dev': [
                'flake8',
                'pytest',
                'pytest-cov',
            ],
        },
    package_data={'': ['*.xls', '*.xsd', '*.json',
                       '*.css', '*.xml', '*.rst']},
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False
)