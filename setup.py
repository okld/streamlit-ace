import setuptools

setuptools.setup(
    name="streamlit-ace",
    version="0.0.1",
    author="Ghasel",
    author_email="",
    description="Streamlit component for React Ace",
    long_description="Streamlit component for React Ace (https://github.com/securingsincity/react-ace)",
    long_description_content_type="text/plain",
    url="https://github.com/Ghasel/streamlit-ace.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
