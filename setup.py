from setuptools import setup

setup(name="sampleinfo",
            version="0.1",
            description="Basic system information for COMP30670",
            url="",
            author="Manjunath Sanjiv Kulkarni",
            author_email="manjunath.kulkarni@ucdconnect.ie",
            license="GPL3",
            packages=['sampleinfo'],
            entry_points={
                'console_scipts':['comp30670_systeminfo=sampleinfo.main:main']})
