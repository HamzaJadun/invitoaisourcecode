import os

def validate_filename(filename):
    """Ensure the filename has a valid extension."""
    if not filename.endswith(".mp4"):
        print("⚠️ Warning: Filename should end with .mp4. Adding extension automatically.")
        filename += ".mp4"
    return filename

def ensure_directory(directory):
    """Ensure the specified directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"📁 Created directory: {directory}")
    else:
        print(f"📁 Using existing directory: {directory}")
