from setuptools import setup, find_packages

setup(
    name='my_anki_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'genanki',
        'openai',
        'argparse',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'my_anki_package=my_anki_package.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package to generate Anki flashcards using genanki',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_anki_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)