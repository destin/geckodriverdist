import distutils.log
import os
import tarfile
import urllib.request
from distutils.command.install_scripts import install_scripts

from setuptools import setup
from setuptools.command.install import install


def download_geckodriver(version):
    target_fname = 'geckodriver.tar.gz'
    download_url = 'https://github.com/mozilla/geckodriver/releases/download/v{version}/geckodriver-v{version}-linux64.tar.gz'.format(
        version=version)
    urllib.request.urlretrieve(
        download_url,
        target_fname)
    return target_fname


class PreInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        distutils.log.info('running geckodriver download')
        fname = download_geckodriver('0.18.0')
        distutils.log.info('running geckodriver extraction')
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()

        install.run(self)


class InstallGeckodriver(install_scripts):

    def finalize_options(self):
        install_scripts.finalize_options(self)
        self.binary = 'geckodriver'
        self.output = os.path.join(self.install_dir, self.binary)

    def get_outputs(self):
        outputs = install_scripts.get_outputs(self)
        return outputs + [self.output]

    def run(self):
        self.mkpath(self.build_dir)
        self.copy_file(self.binary, self.output)
        install_scripts.run(self)


setup(
    name='geckodriverdist',
    version='0.1',
    description='Install geckodriver',
    url='http://github.com/destin/geckodriverdist',
    author='Dawid Pytel',
    author_email='pytel.dawid@gmail.com',
    license='MIT',
    packages=[],
    zip_safe=False,
    cmdclass={
        'install': PreInstallCommand,
        'install_scripts': InstallGeckodriver
    }
)
