from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in administrative_locations/__init__.py
from administrative_locations import __version__ as version

setup(
	name="administrative_locations",
	version=version,
	description="Administrative Locations",
	author="Africlouds",
	author_email="info@africlouds.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
