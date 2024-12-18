# Handshakes performed by 10 people.
# Not more than one handshake is performed. 
# 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0 = 45 total handshakes
handshakes = 0

for people in range(10):
    handshakes = handshakes + people
    print("People before iteration", people)
print(handshakes)