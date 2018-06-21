from setuptools import setup

setup(name='sort_package',
      version='0.1',
      description='Sort everything',
      long_description='Really, everything.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: FDRB License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='sort dev sorting',
      url='http://github.com/storborg/sort',
      author='Sorting Life',
      author_email='devs@example.com',
      license='FDRB',
      packages=['sort_package'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
)
