from setuptools import setup # type: ignore

setup(
    name='jarvis-cli',
    version='0.1',
    py_modules=['jarvis'],
    entry_points={
        'console_scripts': [
            'jarvis=jarvis:main', 
        ],
    },
)
