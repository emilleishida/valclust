from distutils.core import setup

setup(name='valclust',
      version='0.1.0',
      description='Clustering Validation and Analysis',
      author='Vahid Mirjalili, Taban Eslami',
      author_email='vmirjalily@gmail.com',
      url='https://github.com/mirjalil/valclust',
      packages=['valclust'],
      data_files = [('', ['LICENSE']),
                    ('', ['docs/README.html']),
                    ('', ['CHANGELOG.txt']),
                   ],
      license='GPLv3',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
      ],
      long_description="""



 Contact
=============

eMail: vmirjalily@gmail.com
Twitter: https://twitter.com/vmirly

This project is hosted at https://github.com/mirjalil/valclust

""",
    )

