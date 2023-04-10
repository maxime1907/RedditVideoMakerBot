import os

from setuptools import find_packages, setup


def rel(*xs: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("README.md")) as f:
    long_description = f.read()


with open(rel("src", "RedditVideoMakerBot", "__init__.py")) as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


dependencies = [
    "boto3==1.24.24",
    "botocore==1.27.24",
    "gTTS==2.2.4",
    "moviepy==1.0.3",
    "playwright==1.23.0",
    "praw==7.6.1",
    "prawcore~=2.3.0",
    "pytube==12.1.0",
    "requests==2.28.1",
    "rich==13.3.1",
    "toml==0.10.2",
    "translators==5.3.1",
    "pyttsx3==2.90",
    "Pillow~=9.4.0",
    "tomlkit==0.11.4",
    "Flask==2.2.2",
    "clean-text==0.6.0",
    "unidecode==1.3.2",
    "spacy==3.4.1",
    "torch==1.12.1",
    "transformers==4.25.1",
]

extra_dependencies: dict[str, list[str]] = {}

extra_dependencies["all"] = list(set(sum(extra_dependencies.values(), [])))
extra_dependencies["dev"] = extra_dependencies["all"] + [
    # Tools
    "pip-tools",
    # Linting
    "autoflake",
    "flake8",
    "flake8-bugbear",
    "flake8-quotes",
    "isort",
    "black==22.10.0",
    "mypy>=1.0.1",
    "pyupgrade>=3.3.1",
]

setup(
    name="RedditVideoMakerBot",
    version=version,
    author="elebumm",
    author_email="lewis@tmrrwinc.ca",
    description="Create Reddit Videos with just one command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.10",
    install_requires=dependencies,
    extras_require=extra_dependencies,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    entry_points={
        "console_scripts": [
            "RedditVideoMakerBot=RedditVideoMakerBot.cli:cli",
            "RedditVideoMakerBotGUI=RedditVideoMakerBotGUI.cli:cli",
        ]
    },
)
