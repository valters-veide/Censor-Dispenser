email_one = open("email_one.txt", "r")
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


### FUNKCIJA PARBAUDA VAI VARDS NAV DALA NO KADA CITA VARDA ###
def prieksa_pakala(saraksts, num, saraksts_term):
    o = ((saraksts[num - 1] == " " or saraksts[num - 1] == "\n" or saraksts[num - 1] == "(" or saraksts[
        num - 1] == "'" or saraksts[num - 1] == '"') and ((
            saraksts[num + len(saraksts_term)] == " " or saraksts[num + len(saraksts_term)] == "\n" or saraksts[
        num + len(saraksts_term)] == "!" or saraksts[num + len(saraksts_term)] == "." or saraksts[
                num + len(saraksts_term)] == "?" or saraksts[num + len(saraksts_term)] == ")" or saraksts[
                num + len(saraksts_term)] == "'" or saraksts[num + len(saraksts_term)] == '"' or saraksts[
                num + len(saraksts_term)] == "s" or (saraksts[num + len(saraksts_term)] == "l" and saraksts[
        num + len(saraksts_term) + 1] == "y"))))
    return o


### FUNKCIJA PARBAUDA VAI JAU CENZETA VARDA PARPALIKUMS NAV DALA NO KADA CITA VARDA ###
def prieksa_pakala_ly(saraksts, num, saraksts_term, character):
    oo = ((saraksts[num - 1] == character) and (
            saraksts[num + len(saraksts_term)] == " " or saraksts[num + len(saraksts_term)] == "\n" or saraksts[
        num + len(saraksts_term)] == "!" or saraksts[num + len(saraksts_term)] == "." or saraksts[
                num + len(saraksts_term)] == "?" or saraksts[num + len(saraksts_term)] == ")" or saraksts[
                num + len(saraksts_term)] == "'" or saraksts[num + len(saraksts_term)] == '"'))
    return oo


### FUNKCIJAS CENZE PROPRIETRARY TERMS AR DOTO VARDU DESCREETLY, IEVEROJOT CASE ###
def replace_word(email, phrase, proprietary_terms):
    new_censored = email
    saraksts = list(email)
    for term in proprietary_terms:
        saraksts_term = list(term)
        for num in range(len(saraksts)):
            if saraksts[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts, num, saraksts_term):
                    saraksts[num:num + len(saraksts_term)] = phrase
                    new_censored = ("".join(saraksts))
    return new_censored


def replace_word_lower(email, phrase, proprietary_terms):
    new_censored = email
    saraksts = list(email)
    for term in proprietary_terms:
        saraksts_term = list(term.lower())
        for num in range(len(saraksts)):
            if saraksts[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts, num, saraksts_term):
                    saraksts[num:num + len(saraksts_term)] = phrase.lower()
                    new_censored = ("".join(saraksts))
        return new_censored


def replace_word_upper(email, phrase, proprietary_terms):
    new_censored = email
    saraksts = list(email)
    for term in proprietary_terms:
        saraksts_term = list(term.upper())
        for num in range(len(saraksts)):
            if saraksts[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts, num, saraksts_term):
                    saraksts[num:num + len(saraksts_term)] = phrase.upper()
                    new_censored = ("".join(saraksts))
    return new_censored


def replace_word_title(email, phrase, proprietary_terms):
    new_censored = email
    saraksts = list(email)
    for term in proprietary_terms:
        saraksts_term = list(term.title())
        for num in range(len(saraksts)):
            if saraksts[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts, num, saraksts_term):
                    saraksts[num:num + len(saraksts_term)] = phrase.title()
                    new_censored = ("".join(saraksts))
    return new_censored


### UZKRIITOSHI CENZEE PROPRIETRARY TERMS AR DOTU CHARACTER ###
def replace_hard(email, character, proprietary_terms):
    new_censored = email
    saraksts_lower = []
    saraksts = list(email)
    for letter in saraksts:
        letter = letter.lower()
        saraksts_lower.append(letter)
    for term in proprietary_terms:
        saraksts_term = list(term)
        for num in range(len(saraksts)):
            if saraksts_lower[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts_lower, num, saraksts_term):
                    for number in range(len(saraksts_term)):
                        if " " in saraksts_lower[num + number:num + len(character) + number]:
                            saraksts[num + number:num + len(character) + number] = " "
                        else:
                            saraksts[num + number:num + len(character) + number] = character
                    # print("".join(saraksts[num-10:num+len(character)+10+number]))
                    new_censored = ("".join(saraksts))
    return new_censored


### CENZEE PAARPALIKUMUS NO VARDIEM, KAS VAR KAUT KO NODOT ###
def censor_residue(email, character, proprietary_terms):
    new_censored = email
    saraksts_lower = []
    saraksts = list(email)
    for letter in saraksts:
        letter = letter.lower()
        saraksts_lower.append(letter)
    for term in proprietary_terms:
        saraksts_term = list(term)
        for num in range(len(saraksts)):
            if saraksts_lower[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala_ly(saraksts_lower, num, saraksts_term, character):
                    for number in range(len(saraksts_term)):
                        saraksts[num + number:num + len(character) + number] = character
                    new_censored = ("".join(saraksts))
    return new_censored


### CENZEE VARDUS KAS ATRODAS PIRMS UN PEC DOTAJIEM PROPRIETRARY TERMS ###
def censor_sides(email, character, proprietary_terms):
    new_censored = email
    saraksts_lower = []
    saraksts = list(email)
    for letter in saraksts:
        letter = letter.lower()
        saraksts_lower.append(letter)
    for term in proprietary_terms:
        saraksts_term = list(term)
        for num in range(len(saraksts)):
            if saraksts_lower[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts_lower, num, saraksts_term):
                    for number_1 in range(len(saraksts)):
                        if "(" in saraksts[(num - 1) + number_1]:
                            pass
                        elif '"' in saraksts[(num - 1) + number_1]:
                            pass
                        elif " " in saraksts[(num - 2) - number_1]:
                            break
                        elif "\n" in saraksts[(num - 2) - number_1]:
                            break
                        else:
                            saraksts[(num - 2) - number_1] = character
                    for number_2 in range(len(saraksts)):
                        if "s" in saraksts[(num + len(saraksts_term)) + number_2]:
                            pass
                        elif "." in saraksts[(num + len(saraksts_term)) + number_2]:
                            pass
                        elif ")" in saraksts[(num + len(saraksts_term)) + number_2]:
                            pass
                        elif "'" in saraksts[(num + len(saraksts_term)) + number_2]:
                            pass
                        elif '"' in saraksts[(num + len(saraksts_term)) + number_2]:
                            pass
                        elif " " in saraksts[(num + len(saraksts_term) + 1) + number_2]:
                            break
                        elif "\n" in saraksts[(num + len(saraksts_term) + 1) + number_2]:
                            break
                        else:
                            saraksts[(num + len(saraksts_term) + 1) + number_2] = character
            new_censored = ("".join(saraksts))
    return new_censored


### CENZEE NEGATIIVOS VARDUS NO DOTAJIEM NEGATIVE WORDS, JA TADI IR VAIRAK PAR VIENU ###
def replace_negative(email, character, negative_words, negative_word_count, found=[], skippable=[]):
    new_censored = email
    saraksts = list(email)
    saraksts_lower = []
    skippable_counter = 0
    for letter in saraksts:
        letter = letter.lower()
        saraksts_lower.append(letter)
    for word in negative_words:
        saraksts_term = list(word)
        for num in range(len(saraksts)):
            if (saraksts_lower[num:num + len(saraksts_term)]) == saraksts_term:
                if prieksa_pakala(saraksts_lower, num, saraksts_term):
                    negative_word_count = negative_word_count + 1
                    if negative_word_count == 1:
                        skippable = saraksts_lower[num:num + len(saraksts_term)]
                    if negative_word_count > 1:
                        if skippable not in found:
                            for wards in negative_words:
                                looking_for = list(wards)
                                for numa in range(len(saraksts)):
                                    if saraksts_lower[numa:numa + len(looking_for)] == looking_for:
                                        if prieksa_pakala(saraksts_lower, numa, looking_for):
                                            if numa <= ("".join(saraksts)).find("".join(skippable)):
                                                skippable = saraksts_lower[numa:numa + len(looking_for)]
                                                found = skippable
    for word in negative_words:
        saraksts_term = list(word)
        for num in range(len(saraksts)):
            if saraksts_lower[num:num + len(saraksts_term)] == saraksts_term:
                if prieksa_pakala(saraksts_lower, num, saraksts_term):
                    if not (skippable == saraksts_lower[num:num + len(saraksts_term)]) or skippable_counter >= 1:
                        for number in range(len(saraksts_term)):
                            if " " in saraksts_lower[num + number:num + len(character) + number]:
                                saraksts[num + number:num + len(character) + number] = " "
                            else:
                                saraksts[num + number:num + len(character) + number] = character
                    elif skippable == saraksts_lower[num:num + len(saraksts_term)]:
                        skippable_counter = skippable_counter + 1
                    new_censored = ("".join(saraksts))
    return new_censored


### CENZE VIENU VARDU ###
def censored(email, to_be_censored, phrase):
    if to_be_censored in email:
        censored_email = email.replace(to_be_censored, phrase)
    return censored_email


### AR CITU VARDU CENZEE LIELU DAUDZUMU AR VARDIEM ###
def discreet_censor(email, phrase, proprietary_terms):
    censored_email = replace_word(email, phrase, proprietary_terms)
    censored_email_2 = replace_word_lower(censored_email, phrase, proprietary_terms)
    censored_email_3 = replace_word_upper(censored_email_2, phrase, proprietary_terms)
    censored_email_final = replace_word_title(censored_email_3, phrase, proprietary_terms)
    return censored_email_final


### CENZEE AR SIMBOLU VIRKNI TADA PASHA GARUMAA ###
def hard_censor(email, character, proprietary_terms):
    censored_email = replace_hard(email, character, proprietary_terms)
    censored_email_2 = censor_residue(censored_email, character, ["ly"])
    censored_email_3 = censor_residue(censored_email_2, character, ["'s"])
    censored_email_4 = censor_residue(censored_email_3, character, ["s"])
    return censored_email_4


### CENZEE NEGATIIVOS VARDUS NO DOTAJIEM NEGATIVE WORDS, JA TADI IR VAIRAK PAR VIENU UN JAU IEPRIEKS MINETOS PROPRIETRARY TERMS ###
def negative_tone_censor(email, character, proprietary_terms, negative_words):
    negative_word_count = 0
    censored_email = replace_hard(email, character, proprietary_terms)
    censored_email_2 = censor_residue(censored_email, character, ["ly"])
    censored_email_3 = censor_residue(censored_email_2, character, ["'s"])
    censored_email_4 = censor_residue(censored_email_3, character, ["s"])
    censored_email_negative = replace_negative(censored_email_4, character, negative_words, negative_word_count)
    return censored_email_negative


### CENZEE AR SIMBOLU VIRKNI VISU NEPIECIESHAMO + VARDU PIRMS UN VARDU PEC ###
def brutal_censor_evrything(email, character, proprietary_terms, negative_words):
    all_censorable = proprietary_terms + negative_words
    censored_email = censor_sides(email, character, all_censorable)
    censored_email_2 = replace_hard(censored_email, character, all_censorable)
    censored_email_3 = censor_residue(censored_email_2, character, ["ly"])
    censored_email_4 = censor_residue(censored_email_3, character, ["'s"])
    censored_email_5 = censor_residue(censored_email_4, character, ["s"])
    return censored_email_5


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself", "personality"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

announce_email = \
    '''-----------
EMAIL {0}
-----------
'''
announce_censored = \
    '''CENSORED
========='''

print(announce_email.format("ONE"))
print(email_one)
print(announce_censored)
print(censored(email_one, "learning algorithms", "something"))

print(announce_email.format("TWO"))
print(email_two)
print(announce_censored)
print(discreet_censor(email_two, "something", proprietary_terms))
print(announce_censored)
print(hard_censor(email_two, "&", proprietary_terms))

print(announce_email.format("THREE"))
print(email_three)
print(announce_censored)
print(negative_tone_censor(email_three, "%", proprietary_terms, negative_words))

print(announce_email.format("FOUR"))
print(email_four)
print(announce_censored)
print(brutal_censor_evrything(email_four, "*", proprietary_terms, negative_words))
