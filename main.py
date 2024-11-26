from template_handler import display_templates, load_template

def main():
    print("🎥 Welcome to InvitoAI 🎉")
    display_templates()
    choice = int(input("Select a template by number: "))
    template = load_template(choice)

    if template:
        event_name = input("Enter the event name: ")
        date = input("Enter the event date (YYYY-MM-DD): ")
        venue = input("Enter the venue: ")
        host_name = input("Enter the host name(s): ")
        message = input("Enter a custom message: ")

        template.set_details({
            "event_name": event_name,
            "date": date,
            "venue": venue,
            "host_name": host_name,
            "message": message
        })

        filename = input("Enter the output filename (e.g., invitation.mp4): ")
        template.export(filename)
    else:
        print("Invalid template selection.")

if __name__ == "__main__":
    main()
