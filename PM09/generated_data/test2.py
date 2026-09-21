from alien_contact import AlienContact
from alien_contacts import ALIEN_CONTACTS

for item in ALIEN_CONTACTS:
    try:
        contact = AlienContact(**item)
        print("[OK]", contact.contact_id)
    except Exception as e:
        print("[ERROR]", item["contact_id"], e)
