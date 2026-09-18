import random

print("=" * 40)
print("       CYBER INCIDENT REPORT")
print("=" * 40)

time = input("Enter a time: ")
device = input("Enter a device (include a or an): ")
location = input("Enter a location (include the or a): ")
suspicious_item = input("Enter a suspicious object (include a or an): ")

incident_summaries = [
    f"At {time}, {device} in {location} attempted to communicate with {suspicious_item}.",
    f"At {time}, staff in {location} discovered {suspicious_item} controlling {device}.",
    f"Security cameras in {location} recorded {device} following {suspicious_item} at {time}.",
    f"A report from {location} claims that {suspicious_item} tried to log in to {device} at {time}.",
]

summary = random.choice(incident_summaries)

print()
print("INCIDENT SUMMARY")
print(summary)