import os
import re


def slugify_file_name(file_name):
    # Split the file name into base name and extension
    base_name, extension = os.path.splitext(file_name)
    # Remove special characters and spaces from the base name
    slug_base_name = re.sub(r"[^\w\s-]", "", base_name.lower())
    # Replace spaces with underscores
    slug_base_name = re.sub(r"\s+", "_", slug_base_name)
    # Remove leading and trailing underscores
    slug_base_name = slug_base_name.strip("_")
    # Combine the slug base name with the original extension (with dot)
    slug_name = slug_base_name + extension
    # Insert a dot and space after any numeric sequence at the beginning of the file name
    slug_name = re.sub(r"^(\d+)", r"\1.", slug_name)
    return slug_name


directory = "readme_md/pytest_readme"
extension = ".md"

# Check if the directory exists
if os.path.exists(directory):
    # Iterate through files in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            # Get the slug name
            slug_name = slugify_file_name(file_name)
            # Rename the file
            os.rename(
                os.path.join(directory, file_name), os.path.join(directory, slug_name)
            )
            print(f"Renamed '{file_name}' to '{slug_name}'")
else:
    print(f"Directory '{directory}' does not exist.")
