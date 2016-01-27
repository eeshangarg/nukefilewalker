import setuptools

setuptools.setup(
    name='nukeskywalker',
    version='0.0.1',
    description='A simple file indexer',
    url='https://github.com/eeshangarg/nukefilewalker',
    author='Eeshan Garg',
    author_email='jerryguitarist@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Other/Nonlisted Topic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='file indexer word counter',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'nukeskywalker = nukeskywalker.file_indexer:main',
        ]
    },
)
