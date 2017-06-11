from setuptools import setup
from setuptools.command.install import install
import urllib.request
import distutils.log
import os
import tarfile


def download_geckodriver():
    target_fname = 'geckodriver.tar.gz'
    urllib.request.urlretrieve(
        'https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-arm7hf.tar.gz',
        target_fname)
    return target_fname


class PreInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        distutils.log.info('Running geckodriver download')
        fname = download_geckodriver()
        distutils.log.info('Running geckodriver extraction')
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
        
        install.run(self)


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
    },
 scripts=['geckodriver']
	)