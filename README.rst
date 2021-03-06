python-shellwords
==================

|Build| |Coverage| |PyPI version|

Parse line as shell words.


* GitHub: https://github.com/mozillazg/python-shellwords
* License: MIT license
* PyPI: https://pypi.python.org/pypi/shellwords
* Python version: 2.6, 2.7, pypy, 3.3, 3.4

Usage
-------


.. code-block:: python

    >>> from shellwords import ShellWords
    >>> s = ShellWords()
    >>> s.parse("./foo --bar=baz")
    [u'./foo', u'--bar=baz']
    >>> s.parse('./foo --bar=baz foobar')
    [u'./foo', u'--bar=baz', u'foobar']


.. code-block:: python

    >>> os.environ['FOO'] = 'bar'
    >>> s = ShellWords(parse_env=True)
    >>> s.parse("./foo $FOO")
    [u'./foo', u'bar']

.. code-block:: python

    >>> s = ShellWords(parse_backtick=True)
    >>> s.parse("./foo `echo $SHELL`")
    [u'./foo', u'/bin/bash']


Thanks
-------

This is based on `go-shellwords`__ package.

__ https://github.com/mattn/go-shellwords


.. |Build| image:: https://api.travis-ci.org/mozillazg/python-shellwords.png?branch=master
   :target: https://travis-ci.org/mozillazg/python-shellwords
.. |Coverage| image:: https://coveralls.io/repos/mozillazg/python-shellwords/badge.png?branch=master
   :target: https://coveralls.io/r/mozillazg/python-shellwords
.. |PyPI version| image:: https://pypip.in/version/shellwords/badge.png
   :target: https://pypi.python.org/pypi/shellwords
.. |PyPI downloads| image:: https://pypip.in/download/shellwords/badge.png
   :target: https://pypi.python.org/pypi/shellwords
.. |Python versions| image:: https://pypip.in/py_versions/shellwords/badge.svg
   :target: https://pypi.python.org/pypi/shellwords
