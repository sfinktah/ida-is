from setuptools import setup, find_packages
import os

VERSION="0.0.6"
if os.path.exists('README.rst'):
    filename = 'README.rst'
    content_type = 'text/rst'
elif os.path.exists('README.md'):
    filename = 'README.md'
    content_type = 'text/markdown'
with open(filename, "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='ida-is',
    version=VERSION,
    url='https://github.com/sfinktah/ida-is',
    long_description=long_description,
    long_description_content_type=content_type,
    license='MIT',
    author='Christopher Anderson',
    author_email='sfinktah@github.spamtrak.org',
    description='TBA',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    packages=find_packages(),
    install_requires=[],
)
