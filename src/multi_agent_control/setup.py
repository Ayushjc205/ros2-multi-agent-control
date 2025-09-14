from setuptools import find_packages, setup

package_name = 'multi_agent_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayush-jc',
    maintainer_email='ayush-jc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "controller = multi_agent_control.turtlesim_controller:main",
            "spawner = multi_agent_control.turtlesim_spawner:main"
        ],
    },
)
