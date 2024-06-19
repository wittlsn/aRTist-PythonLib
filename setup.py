from setuptools import setup

setup(name='artistlib',
      version='0.1',
      description='THD: aRTist Python library',
      author='Simon Wittl',
      author_email='simon.wittl@th-deg.de',
      license='Apache 2.0',
      packages=['artistlib', 
                'artistlib.hardware', 
                'artistlib.trajectory', 
                'artistlib.utility',
                'artistlib.objects'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Natural Language :: English",
            "Topic :: Multimedia :: Graphics :: Graphics Conversion"
      ],
      zip_safe=False)
      