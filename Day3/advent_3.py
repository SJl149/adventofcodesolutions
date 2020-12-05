from input_day3 import slope

def get_num_trees_on_slope_path(slope_list, across, down):
    trees = 0
    index = 0
    for row in slope_list[down::down]:
        index += across
        if row[index % 31] == '#':
            trees += 1
    return trees


if __name__ == '__main__':
    slope_list = slope.split('\n')
    # trees = get_num_trees_on_slope_path(slope_list, 3, 1)

    # print(trees)
    total = 1
    path_list = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for path in path_list:
        across = path[0]
        down = path[1]
        trees = get_num_trees_on_slope_path(slope_list, across, down)
        total *= trees
        print(f'Path {path} has {trees} trees.')
    print(f'Total number of trees = {total}')