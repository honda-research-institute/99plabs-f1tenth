from setuptools import setup
import os
from glob import glob

package_name = 'autonomous_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'autonomous_control'), glob('autonomous_control/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='99P Labs',
    maintainer_email='research@99plabs.com',
    description='Autonomous control node that sends drive command to vehicle actuator',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'autonomous_control = autonomous_control.autonomous_control:main'
        ],
    },
)
