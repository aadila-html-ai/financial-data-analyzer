from setuptools import setup, find_packages

setup(
    name="financial-data-analyzer",
    version="1.0.0",
    description="A CLI toolkit for analyzing historical price data: returns, volatility, drawdown, Sharpe ratio, and more.",
    author="Your Name",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "financial-analyzer=financial_analyzer.cli:main",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
