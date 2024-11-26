class Template:
    def __init__(self, name):
        self.name = name
        self.details = {}

    def set_details(self, details):
        """Set details for the template."""
        self.details.update(details)
        print(f"Details updated: {self.details}")

    def export(self, filename):
        """Export the template as a video file."""
        print(f"Exporting template '{self.name}' to '{filename}'...")
        # Simulate the video export process
        print("✅ Video exported successfully!")

    @staticmethod
    def load(template_name):
        """Simulate loading a template."""
        print(f"Template '{template_name}' loaded successfully!")
        return Template(template_name)
