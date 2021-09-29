from distutils.core import setup

setup(
    name = 'MyPackage',
    description = 'This is my package',
    packages = ['src.Parser', 'src.Visualizer'], 
    package_dir = { 'src.Parser' : 'src/Parser' }, 
    version = '1',
    url = 'http://www.mypackage.org/',
    author = 'Me',
    author_email = 'me@here.com',
) 