def get():
    info = {}
    info.update(
{ 'classifiers': [ 'Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python'],
  'description': 'JSYNC is JSON plus YAML',
  'install_requires': ['json', 'testml', 'pyyaml'],
  'long_description': 'JSYNC - Full Data Serialization in JSON\n---------------------------------------\n\nInstallation\n------------\n\nUse::\n\n    > sudo pip install jsync\n\nor::\n\n    > sudo easy install jsync\n\nor::\n\n    > git clone git://github.com/you/jsync-py.git\n    > cd reparse-py\n    > sudo make install\n\nUsage\n-----\n\nPython code::\n\n    import jsync\n\n    string = jsync.dump(object)\n    object = jsync.load(string)\n\nDevelopment Status\n------------------\n\nALPHA\n\nCommunity\n---------\n\n#jsync on irc.freenode.net\n\nAuthors\n-------\n\n* Ingy dot Net <ingy@ingy.net>\n\nCopyright\n---------\n\njsync is Copyright (c) 2010, Ingy dot Net\n\njsync is licensed under the New BSD License. See the LICENSE file.\n',
  'name': 'jsync',
  'packages': ['jsync'],
  'scripts': [],
  'url': 'http://jsync.org',
  'version': '0.0.1'}
)
    return info
