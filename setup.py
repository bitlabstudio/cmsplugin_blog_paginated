from setuptools import setup, find_packages
import os

setup(
    name='cmsplugin-blog-paginated',
    version='0.1',
    description='Overrides the index view of cmsplugin_blogs urls.py in order to provide pagination for that view.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Martin Brochhaus',
    author_email='martin.brochhaus@bitmazk.com',
    url='http://github.com/bitmazk/cmsplugin-blog-paginated/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=['cmsplugin-blog'],
)
