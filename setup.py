
m setuptools import setup, find_packages

setup(
    name = "django-rambo",
    version = "1.0",
    url = 'http://github.com/sirmmo/RaMBo',
    license = 'BSD',
    description = "Resource and Meetingroom Booking organizer",
    author = 'Marco Montanari',
    author_email = "sirmmo@gmail.com",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
    packages = find_packages('rambo'),
    package_dir = {'': 'rambo'},
    install_requires = ['setuptools'],

)
