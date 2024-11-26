from template_engine import Template

# Predefined template options
TEMPLATES = [
    "Baby Shower - 1064",
    "Wedding Invitation",
    "Arangetram Ceremony",
    "Baptism Ceremony"
]

def display_templates():
    """Display available templates to the user."""
    print("Available Templates:")
    for idx, template in enumerate(TEMPLATES, start=1):
        print(f"{idx}. {template}")

def load_template(choice):
    """Load a template based on user choice."""
    if 1 <= choice <= len(TEMPLATES):
        template_name = TEMPLATES[choice - 1]
        print(f"Loading template: {template_name}")
        return Template(template_name)
    else:
        print("Invalid selection. Please try again.")
        return None
