import sys
import crypt

def checkPassword(passHash, word):
    salt = passHash[0:2]
    currentHash = crypt.crypt(word, salt)

    if currentHash is passHash:
        print("Found the password {solution}".format(solution=word))
        return true
    else:
        print("Continuing to Search...")
        return false

def main():
    if(len(sys.argv) == 3):
        passwordFile = sys.argv[1]
        dictionaryFile = sys.argv[2]

    for line in passwordFile:
        credentials = line.split(':')
        userName = credentials[0]
        passHash = credentials[1]

        print("Currently Cracking Password for {user}".format(user=userName))

        for line in dictionaryFile:
            if checkPassword(passHash, line.strip('\n')):
                break

if __name__ == "__main__":
    main()
