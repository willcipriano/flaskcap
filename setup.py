from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='flaskcap',
      version='0.0',
      description='Auth for Flask',
      author='Will Cipriano',
      author_email='will@willcipriano.com',
      packages=['flaskcap'],
      install_requires=requirements,
      data_files=[('config', ['config/flaskcap.ini']),
                  ('lua', ['lua/save_user.lua', 'lua/get_user.lua'])]
      )
