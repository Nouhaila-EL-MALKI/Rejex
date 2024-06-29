import re

mot_de_passe = "Wjfq@hiuzh468"

def verificationMotdePass(motdepasse):
    estMaj = re.match(r".*[A-Z].*", motdepasse)
    estMinsc = re.match(r".*[a-z].*", motdepasse)
    estchiffre = re.match(r".*[\d].*", motdepasse)
    estspecial = re.match(r".*[@ -_\&|].*", motdepasse)
    longueur = re.match(r".{8,}", motdepasse)
    if estMaj and estchiffre and estMinsc and estspecial and longueur:
        print("le Mot de passe est fort")
    else:
        print("veillez saisir un mot de passe plus fort")





def validateURL(url):
    url_regex = re.compile(
        r'^(https?|ftp|mailto):\/\/'  # protocol
        r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'  # domain
        r'(:[0-9]{1,5})?'  # port (optional)
        r'(\/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=%]*)?$'  # path (optional)
    )
    
    if url_regex.match(url):
        print(f"URL is valid: {url}")
    else:
        print(f"URL is not valid: {url}")
