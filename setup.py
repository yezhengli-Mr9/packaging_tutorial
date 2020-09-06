import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-YOUR-USERNAME-HERE', # Replace with your own username
    version='0.0.1',
    author='Example Author',
    author_email='yezhengli9@outlook.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yezhengli-Mr9/packaging_tutorial.git',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)