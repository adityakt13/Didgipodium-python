# find , index , rfind

message = "the quick brown fox jumped over the lazy dog."
idx = message.find('own')
if idx != -1:
    print(f"'own' is at index {idx}")
else:
    print("'own' not found ")
idx = message.find('owl')
if idx != -1:
    print(f"'owl' is at index {idx}")
else:
    print("'owl' not found")

idx = message.find('the')
print(f"'the' is at index {idx}")
idx = message.rfind('the')
print(f"'the' is at index {idx}")