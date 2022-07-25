import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='Jooce',  
     version='0.0.1',
     scripts=['Jooce'] ,
     author="Kevin Hyekang Joo",
     author_email="joos2010kj@gmail.com",
     description="Simple and Easy Way to Recycle Boring Codes",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/joos2010kj/Jooce",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )