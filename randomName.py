import random

# from http://www.geocities.com/anvrill/names/cc_goth.html
PLACES = ['Adara', 'Adena', 'Adrianne', 'Alarice', 'Alvita', 'Amara', 'Ambika', 'Antonia', 'Araceli', 'Balandria', 'Basha', 'Beryl', 'Bryn', 'Callia',
          'Caryssa', 'Cassandra', 'Casondrah', 'Chatha', 'Ciara', 'Cynara', 'Cytheria', 'Dabria', 'Darcei', 'Deandra', 'Deirdre', 'Delores',
          'Desdomna', 'Devi', 'Dominique', 'Drucilla', 'Duvessa', 'Ebony', 'Fantine', 'Fuscienne', 'Gabi', 'Gallia', 'Hanna', 'Hedda', 'Jerica',
          'Jetta', 'Joby', 'Kacila', 'Kagami', 'Kala', 'Kallie', 'Keelia', 'Kerry', 'Kerry-Ann', 'Kimberly', 'Killian', 'Kory', 'Lilith', 'Lucretia',
          'Lysha', 'Mercedes', 'Mia', 'Maura', 'Perdita', 'Quella', 'Riona', 'Safiya', 'Salina', 'Severin', 'Sidonia', 'Sirena', 'Solita', 'Tempest',
          'Thea', 'Treva', 'Trista', 'Vala', 'Winta', "Adric", "Aldo", "Amosen", "Andrel", "Arden", "Arquo", "Arvus", "Branon", "Brance", "Bricks",
          "Carro", "Casslyn", "Cavelle", "Corille", "Cross", "Crowl", "Drav", "Edlun", "Grine", "Helles", "Holtz", "Kelyr", "Kobb", "Kristov",
          "Laudius", "Milos", "Morlan", "Narcus", "Noggs", "Orlan", "Phin", "Roethe", "Skannon", "Stavrul", "Stev", "Timoth", "Tocker", "Veleris",
          "Vond", "Weaver", "Wester", "Arlyn", "Ashlyn", "Brena", "Candra", "Carissa", "Casslyn", "Clave", "Cyrene", "Daphnia", "Emeline", "Hix",
          "Kamelin", "Lauria", "Lenia", "Lizete", "Lorette", "Lucella", "Lynthia", "Mara", "Myre", "Naria", "Odrienne", "Polonia", "Quess", "Remira",
          "Sesereth", "Sethla", "Syra", "Talitha", "Tesslyn", "Thena", "Una", "Vaurin", "Veretta", "Vestine", "Vey", "Volette", "Zamira", "Ahnav",
          "Aiz", "Arkash", "Ayan", "D’ruva", "Elesh", "Hakan", "Hanesh", "Haran", "Iku", "Isak", "Izu", "Jahan", "Jin", "Kan", "Kahan", "Ket", "Kos",
          "Kotar", "Lekat", "Lor", "Marek", "Mata", "Mo’an", "Muhan", "Nav", "Nek’set", "Niru", "Ra", "Rahan", "Ro", "Rukon", "Suhin", "Ta’amet",
          "Taji", "Useth", "Vaati", "Von", "Vondu", "Aniya", "Anva", "Darha", "Elesha", "Eva", "Evi", "Esha", "Iana", "Isha", "Jaya", "Kahara",
          "Kavira", "Keta", "Kiara", "Kotara", "Kyra", "La’ana", "Lasa", "Lenaya", "Ma’ana", "Mita", "Nashala", "Na’ava", "Navya", "Rahana", "Ro’an",
          "Ruka", "Sa’ana", "Sarha", "Sethla", "Sevra", "S’rata", "Su’ua", "Syra", "Tukara", "Una", "Usa", "Vaha", "Vanya", "Vara", "Zamira", "Zarha",
          "Zora"]


###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)

    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]

    def get_suffix(self, prefix):
        l = self[prefix]
        return random.choice(l)


class MName:
    """
    A name from a Markov chain
    """

    def __init__(self, chainlen=2):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for l in PLACES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0, len(l)):
                self.mcd.add_key(s[n:n + chainlen], s[n + chainlen])
            self.mcd.add_key(s[len(l):len(l) + chainlen], "\n")

    def new(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()
