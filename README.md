# Themis - Burst the filter bubble 🫧

![GitHub License](https://img.shields.io/github/license/joflucki/themis?color=red)
![GitHub last commit](https://img.shields.io/github/last-commit/joflucki/themis?color=purple)


**A proactive internet assistant designed to help users debunk misinformation and access reliable information through dynamic interactions and fact-based responses**

Themis is an internet assistant designed to help users debunk misinformation and access reliable, fact-based information online. The goal of this project is to create an intelligent, autonomous, proactive tool that can assist users in identifying false claims and promote informed decision-making on the internet.

> The death of truth is the ultimate victory of evil. When truth leaves us, when we let it slip away, when it is ripped from our hands, we become vulnerable to the appetite of whatever monster screams the loudest.

# Installing

To install Themis, first clone the github repository:

```bash
git clone https://github.com/joflucki/themis
```

Then, in that repository, run the following install command:
```
pip install .
```

> [!NOTE]
> If you are a developer planning to contribute to the Themis codebase, please use the following install command:
> ```
> pip install -e .[dev]
> ```
> This will install the necessary dependencies for development, and make the install editable.

# Testing
To run tests, make sure you have all the development dependencies installed. If they are, simply run all tests launching the `pytest` tool in the root directory:

```
pytest
```