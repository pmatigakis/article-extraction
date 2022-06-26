from setuptools import setup

setup(
    name="article_extraction",
    version="0.2.0-dev",
    packages=["article_extraction"],
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.8",
    install_requires=["lxml>=4.7.1"],
    test_suite="tests",
    author="Panagiotis Matigakis",
    author_email="pmatigakis@gmail.com",
    description="Article text extraction library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
