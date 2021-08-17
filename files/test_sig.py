import signfile as signature

print("What file do you want to sign:\n")
file = input()
print("And whose signature are you adding:\n")
sig = input()

try:
    signature.sign(sig, file)
except:
    print("file not found")

print("\nfile signed as:\n" + sig)
