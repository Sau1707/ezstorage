# Automatically update the pyproject.toml version number
import toml
import requests
from packaging.version import Version

class AutoVersion:
    def __init__(self, toml_file) -> None:
        self.toml_file = toml_file
        with open(toml_file, "r") as file:
            data = toml.load(file)

        self.package_name = data["project"]["name"]
        self.current_version = Version(data["project"]["version"])

    def get_latest_version(self):
        url = f"https://pypi.org/pypi/{self.package_name}/json"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to fetch package version"

        if response.status_code == 200:
            data = response.json()
            latest_version = data["info"]["version"]
            return Version(latest_version)
        
    def update_version(self):
        pypi_version = self.get_latest_version()

        # If the version was updated locally, we don't want to downgrade it, then we start from zero
        if self.current_version.major > pypi_version.major or self.current_version.minor > pypi_version.minor:
            new_version = f"{self.current_version.major}.{self.current_version.minor}.0"
        else:
            new_version = f"{pypi_version.major}.{pypi_version.minor}.{pypi_version.micro + 1}"

        # Update the version in the pyproject.toml file
        with open(self.toml_file, "r") as file:
            data = toml.load(file)

        data["project"]["version"] = new_version
        with open(self.toml_file, "w") as file:
            toml.dump(data, file)


if __name__ == "__main__":
    version = AutoVersion("pyproject.toml")
    version.update_version()