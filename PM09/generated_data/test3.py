import json
from alien_contact import AlienContact

with open("invalid_contacts.json") as f:
    data = json.load(f)

for item in data:
    try:
        AlienContact(**item)
        print("[ERROR] Should have failed but passed")
    except Exception as e:
        print("[OK] Correctly failed:", e)
