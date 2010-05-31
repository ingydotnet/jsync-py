JSYNC - Full Data Serialization in JSON
---------------------------------------

Installation
------------

Use::

    > sudo pip install jsync

or::

    > sudo easy install jsync

or::

    > git clone git://github.com/you/jsync-py.git
    > cd reparse-py
    > sudo make install

Usage
-----

Python code::

    import jsync

    string = jsync.dump(object)
    object = jsync.load(string)

Development Status
------------------

ALPHA

Community
---------

#jsync on irc.freenode.net

Authors
-------

* Ingy dot Net <ingy@ingy.net>

Copyright
---------

jsync is Copyright (c) 2010, Ingy dot Net

jsync is licensed under the New BSD License. See the LICENSE file.
