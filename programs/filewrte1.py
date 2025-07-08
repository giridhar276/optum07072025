

# regular way # traditional way
fobj = open("customers.txt","w")
fobj.write("python\n")
fobj.write("unix\n")
fobj.writelines(["java","oracle\n"])
fobj.close()

# pythonic way
# context manager
# if any lines starts using keyword with ... it is called context manager
# Advantage : file gets closed automatically

with open("customers.txt","w") as fobj:
    fobj.write("javascript\n")
    fobj.write("react JS\n")
    fobj.writelines(["java","oracle\n"])

