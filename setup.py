try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Opinionated organisation-centric OSINT inspired from recon-ng and Maltego',
    'author': 'John Lawrence M. Penafiel',
    'url': 'https://github.com/penafieljlm/inquisitor',
    'download_url': 'https://github.com/penafieljlm/inquisitor',
    'author_email': 'penafieljlm@gmail.com',
    'version': '0.1',
    'install_requires': [
        'google-api-python-client',
        'ipwhois',
        'netaddr',
        'nose',
        'python-whois',
        'shodan',
        'tabulate',
        'tld',
        'unidecode',
        'unqlite',
        'validate_email',
    ],
    'packages': find_packages(),
    'scripts': ['inq'],
    'name': 'inquisitor'
}

setup(**config)