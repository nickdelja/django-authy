from setuptools import setup

setup(
    name="django-authy",
    packages=['dj_authy'],
    version='0.1.1',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="ross@lawpal.com",
    url="https://github.com/rosscdh/django-authy",
    description="A Django app for integrating with authy",
    zip_safe=False,
    package_data={
        "dj_authy": ["templates/dj_authy/*.html"]
    },
    install_requires = [
        'authy',
        'django-phonenumber-field',
    ]
)
