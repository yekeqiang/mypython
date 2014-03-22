from distutils.core import setup
setup(
        name = 'mypackage',
        packages = ['mypackage'], # this must be the same as the name above
        version = '0.1',
        description = 'A random test lib',
        author = 'yekeqiang',
        author_email = 'yekeqiang@gmail.com',
        url = 'https://github.com/yekeqiang/mypackage',   # use the URL to the github repo
        download_url = 'https://github.com/yekeqiang/mypackage/mypython/0.1', # I'll explain this in a second
        keywords = ['testing', 'logging', 'example'], # arbitrary keywords
        classifiers = [],
    )
