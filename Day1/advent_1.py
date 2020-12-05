from input_day1 import expense_report

def find_two_entries_sum_2020(expense_list):
    for entry in expense_list:
        entry = int(entry)
        if str(2020 - entry) in expense_list:
            return [entry, (2020 - entry)]


def find_three_entries_sum_2020(expense_list):
    for entry in expense_list:
        entry1 = int(entry)
        remaining_sum = 2020 - entry1
        remains = [x for x in expense_list if int(x) < remaining_sum]
        for entry2 in remains:
            entry2 = int(entry2)
            entry3 = remaining_sum - entry2
            if str(entry3) in expense_list:
                return [entry1, entry2, entry3]
                    # print(entry1, entry2, entry3)


if __name__ == "__main__":
    expense_list = expense_report.split()
    two_entries = find_two_entries_sum_2020(expense_list)
    print('Two entries:')
    print(f'{two_entries[0]} * {two_entries[1]} = {two_entries[0] * two_entries[1]}')
    
    three_entries = find_three_entries_sum_2020(expense_list)
    print('\nThree entries:')
    print(f'{three_entries[0]} * {three_entries[1]} * {three_entries[2]} = {three_entries[0] * three_entries[1] * three_entries[2]}')
    