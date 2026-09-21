import csv
from alien_contact import AlienContact

with open("alien_contacts.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            contact = AlienContact(**row)
            print("[OK]", contact.contact_id)
        except Exception as e:
            print("[ERROR]", row["contact_id"], e)
