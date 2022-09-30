from distutils.core import setup, find_packages

setup(
    name='dap_classifier_data',
    version='0.0.7',
    packages=find_packages(),
    url='https://45.89.26.185:8081/class_dap_classifier/shared_data',
    license='MIT',
    author='d.fedin',
    author_email='d.fedin@ctrl2go.com',
    description='',
    install_requires= [
        'SQLAlchemy',
    ],
)
