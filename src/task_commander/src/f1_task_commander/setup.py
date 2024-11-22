from glob import glob
import os

from setuptools import setup


package_name = 'f1_task_commander'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'f1_task_commander'), glob('f1_task_commander/*')),
        (os.path.join('share', package_name, 'params'), glob('params/*.yaml')),
        (os.path.join('share', package_name, 'waypoints'), glob('waypoints/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='99P Labs',
    maintainer_email='research@99plabs.com',
    description='An importable library for writing mobile robot applications in python3',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'nav_through_poses = f1_task_commander.nav_through_poses:main',
                'waypoint_follower = f1_task_commander.waypoint_follower:main',
                'f1_robot_navigator = f1_task_commander.f1_robot_navigator:main',
        ],
    },
)
