import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='PromptVerse',  
     version='0.1',
     scripts=['src'] ,
     author="Deepak Kumar",
     author_email="krsna.sri1@gmail.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )