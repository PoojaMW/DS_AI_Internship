contacts={"Pooja" : 8867866548, "Jyoti" : 9606405401, "Shiva" : 7348878748}

contacts["Raj"] = "8867402593"
contacts["Pooja"] = "8867866549"

print(contacts)

print("Look up a name that exists:", contacts.get("Pooja"))
print("Name that does not exist:", contacts.get("Ruby", "Contact not found"))

print("\n--- Contact List ---")
for name, phone in contacts.items():
    print(f"Contact: {name} | phone: {phone}")