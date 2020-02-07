from setuptools import setup

setup(
    name='webotron-20',
    version='0.1',
    author='Ankit K Singh',
    author_email='er.ankit.cs@gmail.com',
    description='Webotron 20 is a tool to deploy static website to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/erankitcs/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
