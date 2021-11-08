import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

__encoding__ = 'utf-8'
ABOUT = {}
cwd = os.getcwd()
projectdir = os.path.abspath(os.path.dirname(__file__))
ABOUT['__encoding__'] = __encoding__

# Module Information
NAME = 'random-password'
DESCRIPTION = (__doc__ or '').split('\n')
try:
    with open(os.path.join(projectdir, 'README.md'), 'r', encoding=__encoding__) as file:
        LONG_DESCRIPTION = file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION
LICENSE = 'MIT License'
CLASSIFIERS = \
    """
Development Status :: 3 - Alpha
Intended Audience :: Other Audience
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Internet
Topic :: Security
"""

# Version
MAJOR = 0
MINOR = 0
MICRO = 1
__version__ = VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)
ABOUT['__version__'] = __version__

# Information
AUTHOR = 'Jacob Chesslo'
AUTHOR_EMAIL = 'jacobchesslo@gmail.com'
URL = 'www.github.com/jacobchesslo/random-password'
DOWNLOAD_URL = 'www.github.com/jacobchesslo/random-password'

# Requirements
REQUIRES_PYTHON = '>=3.0.0'
REQUIRED = []
EXTRAS = {}


class UploadCommand(Command):
    """
    Supports setup.py upload
    """
    description = 'Build and publish this package'
    user_options = []

    @staticmethod
    def status(s):
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(projectdir, 'dist'))
        except OSError:
            pass
        self.status('Building Source and Wheel (universal) distribution...')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        self.status('Uploading the package to PyPI via Twine...')
        os.system('twine upload dist/*')
        self.status('Pushing git tags...')
        os.system('git tag v{0}'.format(ABOUT['__version__']))
        os.system('git push --tags')
        sys.exit()


def setup_password():
    setup(
        name=NAME,
        version=ABOUT['__version__'],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        download_url=DOWNLOAD_URL,
        packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
        install_requires=REQUIRED,
        extra_requires=EXTRAS,
        install_package_data=True,
        license=LICENSE,
        classifiers=CLASSIFIERS,
        cmdclass={
            'upload': UploadCommand,
        },
    )


if __name__ == '__main__':
    setup_password()
