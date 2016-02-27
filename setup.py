from setuptools import setup

setup(
	name='myblog',

    version='1.0',
	
    description='OpenShift App',
	
    author='Nico Zhang',
	
    author_email='chenkai358@vip.qq.com',
	
    url='http://www.nicozhang.xyz/',
	
    install_requires=[
        'Django==1.8.4',
		'DjangoUeditor==1.8.143'
	],
	dependency_links=[
        'https://pypi.python.org/simple/django/',
		'https://pypi.python.org/simple/djangoueditor/'
    ],
    )
