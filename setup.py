from distutils.core import setup
setup(
    name='world2d',
    packages=['world2d'],
    version='0.2.0',
    description='A widget for PyQt5 implementing a 2d world space to draw in.',
    author='Moritz Eissenhauer',
    author_email='moritz.eissenhauer@gmail.com',
    license='MIT',
    url='https://github.com/mmEissen/world2d',
    download_url='https://github.com/mmEissen/world2d/archive/0.1.0.tar.gz',
    keywords=['world2d', 'widget', '2d', 'world', 'space', 'pyqt5'],
    classifiers=[

        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who this project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'PyQt5>=5.9,<6'
    ],
    python_requires='>=3',
)
