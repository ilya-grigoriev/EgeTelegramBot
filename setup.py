from distutils.core import setup

setup(
    name='EgeTelegramBot',
    author='Ilya Grigoryev',
    version='0.1',
    package_data={
        'parse_data': ['parse_data'],
        'handlers': ['py.typed']
    },
    packages=['parse_data', 'handlers']
)
