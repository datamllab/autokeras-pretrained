from distutils.core import setup
from setuptools import find_packages

setup(
    name='autokeras-pretrained',
    packages=find_packages(exclude=('tests',)),
    install_requires=['scipy==1.2.0',
                      'torch==1.0.1.post2',
                      'torchvision==0.2.1',
                      'numpy==1.16.1',
                      'scikit-image==0.14.2',
                      'imageio==2.5.0',
                      'requests==2.21.0',
                      'librosa==0.6.2',
                      'numba',
                      'inflect',
                      'unidecode',
                      'nltk==3.3',
                      'lws==1.2',
                      'opencv-python==4.0.0.21',
                      'boto3'],
    version='0.0.3',
    description='Pretrained models for Auto-Keras',
    author='DATA Lab at Texas A&M University',
    author_email='jhfjhfj1@gmail.com',
    url='http://autokeras.com',
    download_url='https://github.com/jhfjhfj1/autokeras-pretrained/archive/0.0.3.tar.gz',
    keywords=['autokeras', 'keras'],
    classifiers=[]
)
