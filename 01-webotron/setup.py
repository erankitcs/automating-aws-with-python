from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='webotron-20',
    version='0.4',
    author='Ankit K Singh',
    author_email='er.ankit.cs@gmail.com',
    description='Webotron 20 is a tool to deploy static website to AWS.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['webotron'],
    url='https://github.com/erankitcs/automating-aws-with-python',
    download_url='https://github.com/erankitcs/automating-aws-with-python/archive/v0.4.tar.gz',
    keywords = ['AWS', 'BOTO3', 'S3Website','CloudFront'],
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    ''',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)
