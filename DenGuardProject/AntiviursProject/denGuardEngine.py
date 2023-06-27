import hashlib
import os
import requests

# Global Variables
malware_hashes = []
virusInfo = []
blocked_websites = []

# Load malware hashes and virus information
def load_data():
    global malware_hashes
    global virusInfo
    global blocked_websites

    with open("virusHash.denvit", "r") as f:
        malware_hashes = f.read().split('\n')

    with open("virusInfo.denvit", "r") as f:
        virusInfo = f.read().split('\n')

    with open("maliciousWebsite.denvit", "r") as f:
        blocked_websites = f.read().split('\n')

# Get the SHA256 hash of a file
def sha256_hash(filename):
    try:
        with open(filename, "rb") as f:
            bytes = f.read()
            sha256_hash = hashlib.sha256(bytes).hexdigest()
        return sha256_hash
    except:
        return None

# Check if a file is malware based on its hash
def malware_checker(filepath):
    hash_value = sha256_hash(filepath)
    if hash_value is not None and hash_value in malware_hashes:
        index = malware_hashes.index(hash_value)
        if index < len(virusInfo):
            return virusInfo[index]
    return None

# Scan a directory for malware
def virusScanner(directory):
    global virusName
    global virusPath

    virusName = []
    virusPath = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            result = malware_checker(filepath)
            if result is not None:
                virusName.append(result + " :: File :: " + filepath)
                virusPath.append(filepath)

# Remove viruses
def virusRemover():
    try:
        if virusPath:
            for path in virusPath:
                os.remove(path)
            print("Viruses removed successfully.")
        else:
            print("No viruses found.")
    except Exception as e:
        print("An error occurred while removing viruses:", str(e))

# Remove junk files
def junkFileRemover():
    try:
        temp_dirs = [
            "C:\\Windows\\Temp",
            "C:\\Users\\{}\\AppData\\Local\\Temp".format(os.environ.get('USERNAME'))
        ]

        for temp_dir in temp_dirs:
            for dirpath, dirnames, filenames in os.walk(temp_dir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        os.remove(filepath)
                    except:
                        pass
                try:
                    os.rmdir(dirpath)
                except:
                    pass

        print("Junk files removed successfully.")
    except Exception as e:
        print("An error occurred while removing junk files:", str(e))

# RamBooster function
def ramBooster():
    try:
        task_list = [
            "notepad.exe",
            "AnyDesk.exe",
            "msedge.exe",
            "TeamViewer_Service.exe",
            "tmaster.exe",
            "inkscape.exe",
            "firefox.exe",
            "vlc.exe",
            "chrome.exe",
            "GOM.exe",
            "msedge.exe",
            "POWERPNT.exe",
            "Word.exe",
            "Excel.exe"
        ]

        for task in task_list:
            os.system("taskkill /f /im {}".format(task))

        print("Processes killed successfully.")
    except Exception as e:
        print("An error occurred while boosting RAM:", str(e))

##################################### Antivirus Engine code End ###############################
