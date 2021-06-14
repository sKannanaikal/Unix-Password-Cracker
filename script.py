import sys
import crypt

def checkPassword(passHash, word):
    salt = passHash[0:2]

    currentHash = crypt.crypt('nutmeg', 'Mi')

    if currentHash.__eq__(passHash):
        print("Found the password {solution}".format(solution=word))
        return True
    else:
        return False

def main():
    if(len(sys.argv) == 3):
        passwordFile = open(sys.argv[1])
        dictionaryFile = open(sys.argv[2])

        for userDetails in passwordFile:
            credentials = userDetails.split(':')
            userName = credentials[0]
            passHash = credentials[1]

            print("Currently Cracking Password for {user}".format(user=userName))

            for line in dictionaryFile:
                if checkPassword(passHash.strip('\n'), line.strip('\n')):
                    break

            dictionaryFile.seek(0)

    print("Process Finished!")

if __name__ == "__main__":
    main()
