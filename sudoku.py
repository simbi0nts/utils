
import random

DIFFICULT = 60
# 70 - HARD
# 60 - MEDIUM
# 50 - EASY

ORIGIN_TEMPLATE_TABLE = [[(((x+(y-1)//3)+((y-1)*3)) % 9)+1 for x in range(0, 9)] for y in range(1, 10)]


################################################################################
################################################################################
#                          Creating puzzle area                                #
################################################################################
################################################################################

def mix_vertical(origin_table, first_column_to_swap=None, second_column_to_swap=None, vertical_area_id=None):
    modified_table = origin_table
    mirror_reverse(modified_table)
    first_column_in_table_to_swap = vertical_area_id * 3 + first_column_to_swap
    second_column_in_table_to_swap = vertical_area_id * 3 + second_column_to_swap
    modified_table[first_column_in_table_to_swap], modified_table[second_column_in_table_to_swap] = \
        modified_table[second_column_in_table_to_swap], modified_table[first_column_in_table_to_swap]
    mirror_reverse(modified_table)
    return modified_table


def mix_horizontal(origin_table, first_line_to_swap=None, second_line_to_swap=None, horizontal_area_id=None):
    modified_table = origin_table
    first_line_in_table_to_swap = horizontal_area_id * 3 + first_line_to_swap
    second_line_in_table_to_swap = horizontal_area_id * 3 + second_line_to_swap
    modified_table[first_line_in_table_to_swap], modified_table[second_line_in_table_to_swap] = \
        modified_table[second_line_in_table_to_swap], modified_table[first_line_in_table_to_swap]
    return modified_table


def mix_vertical_block(origin_table, first_column_area_to_swap=None, second_column_area_to_swap=None, *args, **kwargs):
    modified_table = origin_table
    mirror_reverse(modified_table)
    for x in range(1, 4):
        modified_table[first_column_area_to_swap * 3 - x], modified_table[second_column_area_to_swap * 3 - x] = \
            modified_table[second_column_area_to_swap * 3 - x], modified_table[first_column_area_to_swap * 3 - x]
    mirror_reverse(modified_table)
    return modified_table


def mix_horizontal_block(origin_table, first_line_area_to_swap=None, second_line_area_to_swap=None, *args, **kwargs):
    modified_table = origin_table
    for x in range(1, 4):
        modified_table[first_line_area_to_swap*3-x], modified_table[second_line_area_to_swap*3-x] = \
            modified_table[second_line_area_to_swap*3-x], modified_table[first_line_area_to_swap*3-x]
    return modified_table


def reverse_horizontal(origin_table, *args, **kwargs):
    modified_table = origin_table
    for x in range(len(origin_table)):
        modified_table[x][:] = origin_table[x][::-1]
    return modified_table


def reverse_vertical(origin_table, *args, **kwargs):
    modified_table = origin_table
    modified_table[:] = origin_table[::-1]
    return modified_table


def mirror_reverse(origin_table, *args, **kwargs):
    modified_table = origin_table
    for x in range(len(modified_table)):
        for y in range(len(modified_table)-x):
            modified_table[x][8-y], modified_table[8-y][x] = modified_table[8-y][x], modified_table[x][8-y]
    return modified_table


def make_random_table(origin_table):
    rng = random.randint(100, 300)
    rng_list = [mix_horizontal, mix_vertical, mirror_reverse] + [reverse_horizontal, reverse_vertical]
    for x in range(rng):
        random.choice(rng_list)(origin_table, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2))
    return origin_table


################################################################################
################################################################################
#                          Printing puzzle area                                #
################################################################################
################################################################################

def print_table(origin_table):
    for x in range(len(origin_table)):
        print(origin_table[x])


def print_table_secret(origin_table):
    for x in range(len(origin_table)):
        newline = ''
        for y in range(len(origin_table)):
            if random.randint(0, 100) > DIFFICULT:
                newline += str(origin_table[x][y])
            else:
                newline += '-'
        print(newline)


################################################################################
################################################################################
#                          Testing puzzle area                                 #
################################################################################
################################################################################

def check_line_for_repeat_numbers(origin_table, num):
    for x in range(len(origin_table)):
        if origin_table[x].count(num) > 1:
            return True
    return False


def check_column_for_repeat_numbers(origin_table, num):
    modified_table = origin_table
    mirror_reverse(modified_table)
    error = check_line_for_repeat_numbers(modified_table, num)
    mirror_reverse(modified_table)
    return error


def check_areas_for_repeat_numbers(origin_table, num):
    modified_table = origin_table
    for x in range(3):
        for y in range(3):
            error = check_area_for_repeat_numbers(modified_table, num, x, y)
            if error:
                return True
    return False


def check_area_for_repeat_numbers(origin_table, num, x, y):
    modified_table = origin_table
    subarea_x_array = [x*3+x_ar for x_ar in range(3)]
    subarea_y_array = [y*3+y_ar for y_ar in range(3)]
    count_num = 0
    for x in subarea_x_array:
        for y in subarea_y_array:
            if modified_table[x][y] == num:
                count_num += 1
    if count_num == 1:
        return False
    else:
        return True


def test_table(origin_table):
    modified_table = origin_table
    error = False
    for num in range(1, 10):
        error = check_line_for_repeat_numbers(modified_table, num) or \
                check_column_for_repeat_numbers(modified_table, num) or \
                check_areas_for_repeat_numbers(modified_table, num)
    print(error)

# Main Part

if __name__ == '__main__':
    new_table = ORIGIN_TEMPLATE_TABLE
    make_random_table(new_table)
    # For test (False eq "All Right", True eq "Something Wrong"):
    # test_table(new_table)
    # print_table(new_table)
    print_table_secret(new_table)
