import pip._internal as pip

def install_package(package_name):
    pip.main(['install', package_name])



    
# List of packages to install
packages = [
    "fastapi[all]"
]
    
for package in packages:
    install_package(package)
