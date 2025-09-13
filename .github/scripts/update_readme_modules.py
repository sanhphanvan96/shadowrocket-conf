#!/usr/bin/env python3
"""
This script scans the modules directory and updates the README.md file
with a list of available modules, including installation links.
"""

import os
import re
import urllib.parse
from pathlib import Path

# Repository information
REPO_OWNER = "sanhphanvan96"
REPO_NAME = "shadowrocket-conf"
BRANCH = "master"  # We'll use master branch for the raw links

# File paths
README_PATH = "README.md"
MODULES_DIR = "modules"

def get_module_metadata(filepath):
    """Extract metadata from a module file."""
    metadata = {
        "name": Path(filepath).stem,  # Default to filename without extension
        "icon": None,
        "appurl": None,
        "filepath": filepath
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

            # Extract name
            name_match = re.search(r'#!name\s*=\s*(.*?)[\r\n]', content)
            if name_match:
                metadata["name"] = name_match.group(1).strip()

            # Extract icon
            icon_match = re.search(r'#!icon\s*=\s*(.*?)[\r\n]', content)
            if icon_match:
                metadata["icon"] = icon_match.group(1).strip()

            # Extract appurl
            url_match = re.search(r"#!appurl\s*=\s*(.*?)[\r\n]", content)
            if url_match:
                metadata["appurl"] = url_match.group(1).strip()
    except Exception as e:
        print(f"Error reading module {filepath}: {e}")

    return metadata

def generate_module_entry(metadata):
    """Generate a markdown entry for a module."""
    relative_path = metadata["filepath"]
    raw_url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/refs/heads/{BRANCH}/{relative_path}"
    encoded_url = urllib.parse.quote(raw_url)
    install_url = f"shadowrocket://install?module={encoded_url}"

    entry = []
    entry.append(f"- {metadata['name']}:")

    if metadata["icon"]:
        # entry.append(f"  - Icon: ![]({metadata['icon']})")
        # <img src="image-url" alt="Alt Text" width="300" height="200">
        entry.append(f"  - Icon: <img src=\"{metadata['icon']}\" alt=\"{metadata['name']} Icon\" width=\"40\" height=\"40\">")

    if metadata["appurl"]:
        entry.append(f"  - App URL: {metadata['appurl']}")

    entry.append(f"  - Source: [{raw_url}]({raw_url})")
    entry.append(f"  - [Click to install]({install_url})")

    return entry

def update_readme_modules():
    """Update the README.md file with modules information."""
    # Get all module files
    modules = []
    for filename in os.listdir(MODULES_DIR):
        if filename.endswith(".sgmodule"):
            filepath = os.path.join(MODULES_DIR, filename)
            metadata = get_module_metadata(filepath)
            modules.append(metadata)

    # Sort modules by name
    modules.sort(key=lambda x: x["name"])

    # Generate modules section content
    modules_section = ["## Modules\n"]
    for metadata in modules:
        entry = generate_module_entry(metadata)
        modules_section.extend(entry)
        modules_section.append("")  # Add an empty line between modules

    # Read current README
    with open(README_PATH, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace or add modules section
    modules_pattern = r'## Modules\s*\n(.*?)(?=##|\Z)'
    modules_content = '\n'.join(modules_section)

    if re.search(modules_pattern, content, re.DOTALL):
        updated_content = re.sub(modules_pattern, modules_content + '\n\n', content, flags=re.DOTALL)
    else:
        # If modules section doesn't exist, add it at the end
        updated_content = content.rstrip() + '\n\n' + modules_content + '\n'

    # Write updated README
    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme_modules()
    print("README.md has been updated with modules information.")
