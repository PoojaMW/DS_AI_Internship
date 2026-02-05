IDs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


unique_users = set(IDs)


is_id05_present = "ID05" in unique_users
print("Is ID05 present?", is_id05_present)


print("\nCount Comparison:")
print("Total log entries:", len(IDs))
print("Unique users:", len(unique_users))


print("\nUnique User IDs:")
print(unique_users)