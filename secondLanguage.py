import os

file = open("secondLanguage.txt", "r+")
def setLanguage(language):
    file.write(language)
    os.system(f"export TRANSLATETO={language}")


setLanguage('fr')
