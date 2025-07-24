from setuptools import setup, find_packages

setup(
    name='bot_wsp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.30.0,<3.0.0',
        'certifi>=2023.0.0',
        'charset-normalizer>=3.0.0',
        'idna>=3.0',
        'urllib3>=2.0.0'
    ],
    author='Francisco Arancibia',
    author_email='tuemail@ejemplo.com',
    description='Bot para enviar mensajes por Evolution API desde Python',
    url='https://github.com/ReportFuco/bot_wsp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
