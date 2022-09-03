import os
import setuptools


with open(f"{os.path.dirname(os.path.abspath(__file__))}/requirements.txt") as requirements:
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/README.md") as readme:
        setuptools.setup(
            name="httpfs-py",
            version="0.0.3",
            description="... written in Python",  # FIXME
            long_description=readme.read(),
            long_description_content_type="text/markdown",
            author="Vladimir Chebotarev",
            author_email="vladimir.chebotarev@gmail.com",
            license="MIT",
            classifiers=[
                "Development Status :: 5 - Production/Stable",
                "Environment :: Console",
                "Intended Audience :: Developers",
                "Intended Audience :: Science/Research",
                "Intended Audience :: System Administrators",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Programming Language :: Python :: 3 :: Only",  # FIXME
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "Programming Language :: Python :: 3.12",
                "Topic :: Scientific/Engineering",
                "Topic :: Software Development",
                "Topic :: System :: Benchmark",
                "Topic :: Utilities",
            ],
            keywords=[],  # FIXME
            project_urls={
                "Documentation": "https://github.com/excitoon/httpfs/blob/master/README.md",
                "Source": "https://github.com/excitoon/httpfs",
                "Tracker": "https://github.com/excitoon/httpfs/issues",
            },
            url="https://github.com/excitoon/httpfs",
            packages=[],
            scripts=["httpfs"],
            install_requires=requirements.read().splitlines(),
        )
