# Automatically update the pyproject.toml version number
import toml
from packaging.version import Version

def update_version(file_path: str):
    # Load the TOML file
    with open(file_path, "r") as file:
        data = toml.load(file)
    
    # Increment the patch version
    current_version = Version(data["project"]["version"])
    new_version = str(current_version.major) + "." + str(current_version.minor) + "." + str(current_version.micro + 1)
    
    # Update the version in the dictionary
    data["project"]["version"] = new_version
    
    # Write the updated data back to the file
    with open(file_path, "w") as file:
        toml.dump(data, file)


if __name__ == "__main__":
    update_version("pyproject.toml")