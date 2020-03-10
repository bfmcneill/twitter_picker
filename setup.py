from setuptools import setup, find_packages


setup(
    name='twitter_picker',
    version='0.0.2',
    author='Ben McNeill',
    url='https://github.com/bfmcneill/twitter_picker',
    packages=find_packages(),
    install_requires=['click'],

    # Scripts
    entry_points={
        'console_scripts': [
            'twpicker=twitter_picker.cli.cli:main',
        ],
    },

)
