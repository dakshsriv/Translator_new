#import os
import json


def setLanguage(language):
    file = open("secondLanguage.json", "w")
    data = {"secondLang" : language}
    json.dump(data, file)
    file.close()
#    os.system(f"export TRANSLATETO={language}")

def getLanguage():
    file = open("secondLanguage.json", "r")
    data = json.load(file)
    return data["secondLang"]

#setLanguage('fr')
#print(getLanguage())









