import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        invitation_text = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(invitation_text)
            print(f"Generated file: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
