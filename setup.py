from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(name='MRISegmentator',
        version='0.4.2',
        description='Robust segmentation of 62 abdominal structures on MRI T1 Weighted images.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/rsummers11/MRISegmentator',
        author='Yan Zhuang and Abhinav Suri',
        author_email='rsummers@nih.gov',
        python_requires='>=3.9',
        license='Please See Github',
        packages=find_packages(),
        install_requires=[
            'torch>=2.0.0',
            'tqdm>=4.45.0',
            'p_tqdm',
            'nnunetv2>=2.2.1',
            'requests'
        ],
        zip_safe=False,
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
        entry_points={
            'console_scripts': [
                'MRISegmentator=mrisegmentator.cmdline:main',
                'MRISegmentator_Redownload=mrisegmentator.download_weights:force_redownload',
            ],
        },
    )
