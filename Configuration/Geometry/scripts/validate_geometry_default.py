import os
import re
import sys

def extract_version_from_geometry(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'GeometryExtended2026(\w+)_cff', line)
            if match:
                return f"2026{match.group(1)}"
    raise ValueError(f"Could not find geometry version in {file_path}")

def extract_default_version(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'DEFAULT_VERSION\s*=\s*"(2026\w+)"', line)
            if match:
                return match.group(1)
    raise ValueError(f"Could not find DEFAULT_VERSION in {file_path}")

def main():
    # Retrieve CMSSW_BASE environment variable
    cmssw_base = os.getenv('CMSSW_BASE')
    if not cmssw_base:
        print("Error: CMSSW_BASE environment variable is not set.")
        sys.exit(1)

    # Construct the full paths
    geometry_file = os.path.join(cmssw_base, 'src/Configuration/Geometry/python/GeometryExtended2026Default_cff.py')
    conditions_file = os.path.join(cmssw_base, 'src/Configuration/Geometry/python/defaultPhase2ConditionsEra_cff.py')

    # Check if the files exist
    if not os.path.exists(geometry_file) or not os.path.exists(conditions_file):
        print(f"Error: One or both files do not exist.\nChecked paths:\n{geometry_file}\n{conditions_file}")
        sys.exit(1)

    # Extract versions and compare
    geometry_version = extract_version_from_geometry(geometry_file)
    default_version = extract_default_version(conditions_file)

    # Normalize both versions to include the "2026" prefix for comparison
    if geometry_version != default_version:
        print(f"Error: Geometry version '{geometry_version}' (from {geometry_file}) does not match default version '{default_version}' (from {conditions_file}).\n Please fix!")
        sys.exit(1)

    print(f"Versions are synchronized: '{geometry_version}' in {geometry_file} matches '{default_version}' in {conditions_file}.")
    sys.exit(0)

if __name__ == "__main__":
    main()
