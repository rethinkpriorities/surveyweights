import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
     name='surveyweights',  
     version='0.4',
     author='Peter Hurford',
     author_email='peter@peterhurford.com',
     description='Apply Census weighting to survey data',
     long_description=long_description,
	 long_description_content_type='text/markdown',
     url='https://github.com/rethinkpriorities/surveyweights',
     packages=setuptools.find_packages(),
     classifiers=[
         'Development Status :: 3 - Alpha',
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ],
 )
