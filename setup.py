#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name='nexus',
    version='0.3.0.sm1',
    author='Disqus',
    author_email='opensource@disqus.com',
    url='http://github.com/disqus/nexus',
    description = 'An extendable admin interface',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    tests_require = [
        'Django',
        'South',
    ],
    test_suite = 'nexus.tests',
    include_package_data=True,
    cmdclass={"test": mytest},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
