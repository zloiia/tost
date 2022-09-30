from distutils.core import setup

setup(
    name='dap_classifier_data',
    version='0.0.7',
    packages=[
        'dap_classifier_data',
        'dap_classifier_data.models',
        ],
    url='https://45.89.26.185:8081/class_dap_classifier/shared_data',
    license='MIT',
    author='d.fedin',
    author_email='d.fedin@ctrl2go.com',
    description='',
    install_requires= [
        'SQLAlchemy',
    ],
)
