from setuptools import setup, find_packages

setup(
    name="medai",
    version="0.1.0",
    description="A Streamlit app for medical AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/med-ai",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.20.0",
        "pymongo>=4.5.0",
        "hashlib",
        "python-dotenv",  # Only if you're using .env for storing credentials
    ],
    entry_points={
        "console_scripts": [
            "medai=app:main",  # If you want to use `medai` as a command-line script
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
