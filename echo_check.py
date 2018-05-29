import sys
from nltk.corpus import cmudict
arpabet_dict = cmudict.dict()

# MADE by ILY, aka Maxwell Dulin on 5/25/2018
"""
Strips all of the numbers, which are stresses on the phones.
Args:
    phones(list of strings): a list of a strings, that are the phones.
Returns:
    new_list(list of strings): a list of strings, which correspond to phones.
"""
def strip_numbers_from_list(phones):
    new_list = list()
    for elt in phones:
        new_list.append(''.join([i for i in elt if not i.isdigit()]))
    return new_list


"""
Compares a list of words for alike-ness
Args:
    test(list of a lists of strings): the phrase that is being checked for similarity in the system.
    cur(list of a lists of strings): the phrase that the system is checked from.
Returns:
    (bool): false if the phones are similar, true otherwise
"""
def compare_phones(test,cur):
    if(len(test) != len(cur)):
        return False
    for phrases in range(len(test)):
        if(not compare_phones_per_word(test[phrases],cur[phrases])):
            return False
    return True


"""
Compares a list of words for alike-ness
Args:
    test(list of strings): the word that is being checked for similarity in the system.
    cur(list of strings): the word that the system is checked from.
Returns:
    (bool): false if the phones are similar, true otherwise
"""
def compare_phones_per_word(test,cur):
    if(len(test) != len(cur)):
        return False

    amount = 0
    for spot in range(len(test)-1):
        if(test[spot] != cur[spot]):
            if(amount == 1 or not is_similar(cur[spot],test[spot])):
                return False
            amount+=1
    return True


"""
Convers a full phrase from a word into Arpabet(group of phones)
Args:
    phrase(string): a word being converted
Returns:
    phone_lst(list of strings): Puts each phone(or unit of sound) as an index in the list.
"""
def convert_phrase(phrase):
    phone_lst = list()
    phrase = phrase.split()
    for word in phrase:
        try:
            skill_prounc = arpabet_dict[word][0]
            skill_prounc = strip_numbers_from_list(skill_prounc)
            phone_lst.append(skill_prounc)
        except:
            print word
            raise ValueError("""

    The word does not exist in the CMU pronounciations dictionary. SORRY :(

    """)
    return phone_lst

"""
Compares two words.
Args:
    phrase1(string): a phrase
    phrase2(string): a phrase
Returns:
    (bool): true if the given word is similar, false otherwise.
"""
def valid_skill_compare(phrase1,phrase2):
    phrase_in_phones1 = convert_phrase(phrase1)
    #print phrase_in_phones1
    phrase_in_phones2 = convert_phrase(phrase2)
    #print phrase_in_phones2
    return compare_phones(phrase_in_phones1,phrase_in_phones2)

"""
Checks a list of words against a given phrase to check
Args:
    phrase1(string): the phrase being checked.
Returns:
    (bool) true if not similar, false otherwise
"""
def valid_skill(phrase1, skills = ["not not", "dead in the water", "capital one"]):

    for skill in skills:

        if(valid_skill_compare(skill, phrase1)):
            print "Found a malicious intent with '" + phrase1 + "' skill"
            return False

    print "Valid name!"
    return True

"""
Checks for how similar the phones are. This is referenced by the dictionary below.
Args:
    phone1(string): a phone
    phone2(string): a phone
Returns:
    (bool): Returns true if phones are similar, false otherwise
"""
def is_similar(phone1,phone2):
    similar_dict = {
    'AA':['AO'],
    'AE':[],
    'AH':[],
    'AO':['AA'],
    'AW':[],
    'AY':['EH'],
    'B' :['P','V'],
    'CH':['G','JH'],
    'D' :['T'],
    'DH':['TH'],
    'EH':['AY'],
    'ER':[],
    'EY':[],
    'F' :[],
    'G' :['CH','JH'],
    'HH':[],
    'IH':[],
    'IY':[],
    'JH':['CH','G'],
    'K' :[],
    'L' :[],
    'M' :['N','NG'],
    'N' :['M','NG'],
    'NG':['N','M'],
    'OW':[],
    'OY':[],
    'P' :['B','V'],
    'R' :[],
    'S' :['Z'],
    'SH':['ZH'],
    'T' :['D'],
    'TH':['DH'],
    'UH':[],
    'UW':[],
    'V' :['B','P'],
    'W' :[],
    'Y' :[],
    'Z' :['C'],
    'ZH':['SH']
    }

    return phone2 in similar_dict[phone1] or phone1 in similar_dict[phone2]

def main():


    if(len(sys.argv) == 1):
        print "Testing on skiil capital won..."
        print "Testing against current skills 'capital one', 'steph curry' and 'help'"
        print
        print valid_skill("capital won", skills = ["capital one", "help","steph curry"])
    else:
        skill = sys.argv[1]
        list_of_skills = sys.argv[2].split(",")
        valid_skill(skill, skills = list_of_skills)
main()
