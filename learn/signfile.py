def sign(sig, filename):
    file = open(filename, "a")
    file.write("\n\n")
    file.write(sig)
    return file