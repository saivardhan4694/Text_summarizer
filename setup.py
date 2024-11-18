import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_summarizer"
AUTHOR = "saivardhan4694"
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'makkapatimrk@gamil.com'

setuptools.setup(
    name=REPO_NAME,
    version= __version__,
    author= AUTHOR,
    author_email=AUTHOR_EMAIL,
    description= "A small package for summarizing text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    package_dir = {"": "src"},
    packages= setuptools.find_packages(where="src")
)