from setuptools import setup, find_packages

setup(
    name="whisper",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "tqdm",
        "more-itertools",
        "ffmpeg-python",
        "scipy",
        "numba",
        "openai-tokenizer",
        # "triton==2.0.0",  # ❌ Intentionally removed to fix conflict
    ],
    entry_points={
        "console_scripts": [
            "whisper=__main__:main",
        ],
    },
    include_package_data=True,
    package_data={"": ["assets/*"]},
)

