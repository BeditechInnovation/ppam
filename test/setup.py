from setuptools import setup

setup(
    name="ppam",
    version="0.1.0",
    py_modules=["ppam"],
    entry_points={
        "console_scripts": [
            "ppam=ppam:main",
        ],
    },    
)