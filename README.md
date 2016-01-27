nukefilewalker
==============

```nukefilewalker``` is a simple command-line file indexing application that
takes as input names of plain text files and prints the most encountered
words across all the given files and the number of times each word was
encountered.

And, yes, the name is inspired by Luke Skywalker. Admittedly, it sounded
much better in my head.

Installation
------------

You can install ```nukefilewalker``` by typing:

```pip install nukefilewalker```

Usage
-----
```
usage: nukefilewalker [-h] [-c COUNT] [filepaths [filepaths ...]]

A command-line program that indexes multiple plain text files and prints the
most enountered words and the number of times each word was encountered.

positional arguments:
  filepaths             Paths to files to be indexed.

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        The number of most encountered words to print.
```

For example, to find the top 10 most commonly used words across a collection files, type:

```nukefilewalker file1 file2```

You can also control the number of words returned by supplying an optional argument.
For example, the following will return the top 5 words instead of the default 10:

```nukefilewalker --count 5 file1 file2```

Development
-----------

Pull requests are welcome, so please feel free to fork, clone and make one!

#### Installing the dependences

After cloning the repository, from the top-level directory of the project, type:

```pip install -r dev_requirements.txt```

#### Running the tests

You can run the tests by typing:

```python -m unittest discover```

#### Generating the documentation

This project uses [epydoc](http://epydoc.sourceforge.net/) for generating documentation.
Just type:

```epydoc --html -v -o docs nukefilewalker```

After that, the documentation can be browsed by opening up ```docs/index.html```
in a web browser.
