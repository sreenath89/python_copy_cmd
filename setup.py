import setuptools

with open('README.md') as fh:
    long_descriptiom = fh.read()

setuptools.setup(
    name='python-copy-command',
    version = '1.0.0',
    author = 'sreenath',
    author_email = 'zreenathmenon@gmail.com',
    description = 'Python Copy Command',
    long_description = 'Python alternative for Linux copy command',
    keywords='pcopy python copy',
    classifiers = [
        'Programming Languages :: Python :: 2.7, 3',
        'Licence :: MIT Licence'
        'Operating Systems :: OS Independent'
    ],
    entry_points = {
        'console_scripts': [
             'pcopy = pcopy.__main__:main'
            ]
    }
)
