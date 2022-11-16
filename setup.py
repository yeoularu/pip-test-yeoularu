from setuptools import setup, find_packages

setup(
    name="pip-test-yeoularu",
    version="0.0.1",
    description="for test pypi deploy",
    author="yeoularu",
    author_email="yeoularu@gmail.com",
    url="https://github.com/yeoularu/pip-test-yeoularu",
    download_url="https://github.com/yeoularu/pip-test-yeoularu/archive/main.zip",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["pypi deploy"],
    python_requires=">=3",
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
