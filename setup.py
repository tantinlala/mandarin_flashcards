from setuptools import setup, find_packages

setup(
    name='mandarin_flashcards',
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
            'create_mandarin_flashcards=create_mandarin_flashcards.main:main',
        ],
    },
    author='Nicholas Tantisujjatham',
    author_email='nicholas.tantisujjatham@gmail.com',
    description='A Python package to generate Anki flashcards for Mandarin vocabulary using genanki',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tantinlala/mandarin-flashcards',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)