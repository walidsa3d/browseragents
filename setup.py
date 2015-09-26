from setuptools import find_packages
from setuptools import setup


setup(
    name="browseragents",
    version="0.0.0",
    author="Walid Saad",
    author_email="walid.sa3d@gmail.com",
    url='https://github.com/walidsa3d/browseragents'
    keywords="useragents browser agent",
    description="get random user agent",
    long_description="get random user agent",
    license="MIT",
    packages=find_packages,
    zip_safe=False,
    include_package_data=True,
    classifiers=['Development Status :: 4  - Beta',
                 'Environment :: Console',
                 'Intended Audience :: End Users/Desktop',
                 'Operating System :: OS Independent',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',
                 'Topic :: Utilities']
)
