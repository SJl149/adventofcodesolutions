from input_5 import puzzle_input


def split_list(items):
    half = len(items) // 2
    return items[:half], items[half:]


def get_row(binary_row):
    plane_rows = [x for x in range(128)]
    for partition in [char for char in binary_row]:
        lower_half, upper_half = split_list(plane_rows)
        if partition == 'F':
            plane_rows = lower_half
        else:
            plane_rows = upper_half
    return plane_rows[0]


def get_column(binary_column):
    plane_columns = [x for x in range(8)]
    for partition in [char for char in binary_column]:
        lower_half, upper_half = split_list(plane_columns)
        if partition == 'L':
            plane_columns = lower_half
        else:
            plane_columns = upper_half
    return plane_columns[0]


def get_seat_ids(boarding_passes):
    seat_ids = []
    for boarding_pass in boarding_passes:
        row = get_row(boarding_pass[:7])
        column = get_column(boarding_pass[7:])
        seat_ids.append(row * 8 + column)
    return seat_ids


def find_seat(seat_ids):
    seat_ids.sort()
    full_list_ids = [x for x in range(seat_ids[0], seat_ids[-1] + 1)]
    return set(full_list_ids) - set(seat_ids)


if __name__ == "__main__":
    boarding_passes = puzzle_input.split()
    seat_ids = get_seat_ids(boarding_passes)
    print(f'The highest seat id is {max(seat_ids)}')

    your_seat = find_seat(seat_ids)
    print(f'Your seat id is {your_seat}')
