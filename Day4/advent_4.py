from input_day4 import passports
import re

def convert_input_to_list_of_cred_dictionaries():
    passports_list = []
    for passport in passports.split('\n\n'):
        cred_list = passport.split()
        cred_dict = dict([entry.split(':') for entry in cred_list])
        passports_list.append(cred_dict)
    return passports_list


def validate_byr(byr):
    return byr.isdigit() and (1920 <= int(byr) <= 2002)


def validate_iyr(iyr):
    return iyr.isdigit() and (2010 <= int(iyr) <= 2020)


def validate_eyr(eyr):
    return eyr.isdigit() and (2020 <= int(eyr) <= 2030)


def validate_hgt(hgt):
    measure = hgt[-2:]
    if measure == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif measure == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False


def validate_hcl(hcl):
    return hcl[0] == '#' and len(hcl[1:]) == 6 and re.search('[0-9a-f]{6}', hcl[1:]) #len(hcl[1:]) == 6 and hcl[1:].isalnum()


def validate_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid):
    return pid.isdigit() and len(pid) == 9


def validate_passport(passport):
    is_valid = validate_byr(passport['byr'])
    is_valid = is_valid and validate_iyr(passport['iyr']) 
    is_valid = is_valid and validate_eyr(passport['eyr']) 
    is_valid = is_valid and validate_hgt(passport['hgt'])
    is_valid = is_valid and validate_hcl(passport['hcl'])
    is_valid = is_valid and validate_ecl(passport['ecl'])
    is_valid = is_valid and validate_pid(passport['pid'])
    return is_valid


if __name__ == "__main__":
    passports_list = convert_input_to_list_of_cred_dictionaries()
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_passports = []
    for passport in passports_list:
        if len(passport) > 6 and fields <= set(passport.keys()):
            if validate_passport(passport):
                valid_passports.append(passport)
    print(len(valid_passports))
