def Save_Data(firstn, lastn, email, address, origin):
    with open("profiles.txt", "w") as file:
        file.write("\n**********************************")
        file.write("\nFirst Name: " + str(firstn))
        file.write("\nLast Name: " + str(lastn))
        file.write("\nEmail Address : " + str(email))
        file.write("\nAddress: " + str(address))
        file.write("\nNationality: " + str(origin) + "\n")

    print("[+] Profile has been saved!!")
