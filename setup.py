
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Chuck Logan Lim',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'chucky_da_great@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['life'],
    'scripts': [],
    'name': 'life'
}

setup(**config)

