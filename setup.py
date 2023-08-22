from setuptools import setup


setup(
    name='time-tracking-pkg',
    version='1.0.0',
    install_requires=[
        'wheel',
    ],
    entry_points={
        'console_scripts': [
            'time-tracking-pkg=time_tracking.main_file:main_func'
        ]
    },
)
