from setuptools import setup,find_packages
setup(
    name="placement",
    version="0.0.1",
    packages=find_packages(where='src'),
    packages_dir={"":'src'}
)