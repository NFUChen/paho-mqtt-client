from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A package simplify paho-mqtt client API'

# Setting up
setup(
    name="paho-mqtt-client",
    version=VERSION,
    author="William Chen (SRAM)",
    author_email="wichen@sram.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['paho-mqtt'],
    keywords=['python', 'mqtt', "messageing protocol", "IoT"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
