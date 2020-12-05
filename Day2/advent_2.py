from input_day2 import passwords
from collections import Counter

def find_num_valid_passwords_part1(password_list):
    num_valid = 0
    for row in password_list:
        l = row.split()
        low_high = l[0].split('-')
        letter = l[1][0]
        password = l[2]
        # print(low_high, letter, password)
        counter = Counter(password)
        if int(low_high[0]) <= counter[letter] <= int(low_high[1]):
            num_valid += 1
    return num_valid


def find_num_valid_passwords_part2(password_list):
    num_valid = 0
    for row in password_list:
        l = row.split()
        positions = l[0].split('-')
        position1 = int(positions[0]) - 1
        position2 = int(positions[1]) - 1
        letter = l[1][0]
        password = l[2]
        if (password[position1] == letter and password[position2] != letter) or (password[position1] != letter and password[position2] == letter):
            num_valid += 1
    return num_valid


if __name__ == '__main__':
    password_list = passwords.split('\n')

    # Part 1
    part1_num_valid = find_num_valid_passwords_part1(password_list)
    print(f"Part 1 number of valid passwords: {part1_num_valid} ")

    # Part 2
    part2_num_valid = find_num_valid_passwords_part2(password_list)
    print(f"Part 2 number of valid passwords: {part2_num_valid} ")

