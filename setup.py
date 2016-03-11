from setuptools import setup

setup(
      name = "article_extraction",
      version = "0.1",

      packages = ["article_extraction"],

      install_requires = ["lxml==3.5.0"],

      author = "Panagiotis Matigakis",
      author_email = "pmatigakis@gmail.com",
      description = "Article text extraction library",
)