
import random

DIFFICULT = {
        '1': {"min_nums_in_area": 6, "max_nums_in_area": 7, "min_nums_in_table": 56, "max_nums_in_table": 60},
        '2': {"min_nums_in_area": 5, "max_nums_in_area": 7, "min_nums_in_table": 48, "max_nums_in_table": 57},
        '3': {"min_nums_in_area": 4, "max_nums_in_area": 6, "min_nums_in_table": 40, "max_nums_in_table": 48},
        '4': {"min_nums_in_area": 3, "max_nums_in_area": 5, "min_nums_in_table": 32, "max_nums_in_table": 39},
        '5': {"min_nums_in_area": 2, "max_nums_in_area": 4, "min_nums_in_table": 27, "max_nums_in_table": 33},
    }

# It Just Works!
ORIGIN_TEMPLATE_TABLE = [[(((x+(y-1)//3)+((y-1)*3)) % 9)+1 for x in range(0, 9)] for y in range(1, 10)]


class CreateSudoku(object):

    def make_random_table(self, origin_table):
        rng = random.randint(100, 5000)
        rng_list = [self.mix_horizontal, self.mix_vertical] + \
                   [self.mix_horizontal_block, self.mix_vertical_block] + \
                   [self.reverse_horizontal, self.reverse_vertical, self.mirror_reverse]
        for x in range(rng):
            random.choice(rng_list)(origin_table, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2))
        return origin_table

    @staticmethod
    def mix_horizontal(origin_table, first_line_to_swap=None, second_line_to_swap=None, horizontal_area_id=None):
        modified_table = origin_table
        first_line_in_table_to_swap = horizontal_area_id * 3 + first_line_to_swap
        second_line_in_table_to_swap = horizontal_area_id * 3 + second_line_to_swap
        modified_table[first_line_in_table_to_swap], modified_table[second_line_in_table_to_swap] = \
            modified_table[second_line_in_table_to_swap], modified_table[first_line_in_table_to_swap]
        return modified_table

    def mix_vertical(self, origin_table, first_column_to_swap=None, second_column_to_swap=None, vertical_area_id=None):
        modified_table = origin_table
        self.mirror_reverse(modified_table)
        self.mix_horizontal(modified_table, first_column_to_swap, second_column_to_swap, vertical_area_id)
        self.mirror_reverse(modified_table)
        return modified_table

    @staticmethod
    def mix_horizontal_block(origin_table, first_line_area_to_swap=None, second_line_area_to_swap=None, *args, **kwargs):
        modified_table = origin_table
        for x in range(1, 4):
            modified_table[first_line_area_to_swap*3-x], modified_table[second_line_area_to_swap*3-x] = \
                modified_table[second_line_area_to_swap*3-x], modified_table[first_line_area_to_swap*3-x]
        return modified_table

    def mix_vertical_block(self, origin_table, first_column_area_to_swap=None, second_column_area_to_swap=None, *args, **kwargs):
        modified_table = origin_table
        self.mirror_reverse(modified_table)
        self.mix_horizontal_block(modified_table, first_column_area_to_swap, second_column_area_to_swap)
        self.mirror_reverse(modified_table)
        return modified_table

    @staticmethod
    def reverse_horizontal(origin_table, *args, **kwargs):
        modified_table = origin_table
        for x in range(len(origin_table)):
            modified_table[x][:] = origin_table[x][::-1]
        return modified_table

    @staticmethod
    def reverse_vertical(origin_table, *args, **kwargs):
        modified_table = origin_table
        modified_table[:] = origin_table[::-1]
        return modified_table

    @staticmethod
    def mirror_reverse(origin_table, *args, **kwargs):
        modified_table = origin_table
        for x in range(len(modified_table)):
            for y in range(len(modified_table)-x):
                modified_table[x][8-y], modified_table[8-y][x] = modified_table[8-y][x], modified_table[x][8-y]
        return modified_table


class PrintSudoku(object):

    @staticmethod
    def print_table(origin_table):
        for x in range(len(origin_table)):
            print(origin_table[x])

    @staticmethod
    def format_and_print_table(origin_table):
        for x in range(len(origin_table)):
            strline = ''
            for y in range(len(origin_table)):
                if origin_table[x][y] == 0:
                    strline += ' '
                else:
                    strline += str(origin_table[x][y])
                if y in [2, 5]:
                    strline += '|'
            print(strline)
            if x in [2, 5]:
                strline = '---+---+---'
                print(strline)

    def print_table_secret(self, origin_table, difficult=DIFFICULT['1']):
        secret_table = origin_table
        count_numbers_in_table = self.count_visible_numbers_in_table(secret_table)
        while count_numbers_in_table > difficult['min_nums_in_table']:
            self.modified_secret_table(origin_table, difficult)
            count_numbers_in_table = self.count_visible_numbers_in_table(secret_table)
        self.format_and_print_table(secret_table)

    def modified_secret_table(self, origin_table, difficult=DIFFICULT['1']):
        secret_table = origin_table
        for x in range(len(secret_table)):
            for y in range(len(secret_table)):
                count_numbers_in_table = self.count_visible_numbers_in_table(secret_table)
                if count_numbers_in_table > difficult['max_nums_in_table']:
                    if difficult['min_nums_in_area'] != self.count_visible_numbers_in_area(secret_table, x, y):
                        random_remove_item_choise = random.randint(0, 1)
                        if random_remove_item_choise:
                            secret_table[x][y] = 0
                elif count_numbers_in_table != difficult['min_nums_in_table']:
                    if difficult['min_nums_in_area'] != self.count_visible_numbers_in_area(secret_table, x, y):
                        random_remove_item_choise = random.randint(0, 5)
                        if random_remove_item_choise:
                            secret_table[x][y] = 0
                else:
                    return secret_table

    @staticmethod
    def count_visible_numbers_in_table(origin_table):
        modified_table = origin_table
        count = 0
        for x in range(len(modified_table)):
            for y in range(len(modified_table)):
                if modified_table[x][y] != 0:
                    count += 1
        return count

    def count_visible_numbers_in_area(self, origin_table, x, y):
        modified_table = origin_table
        count = 0
        subarea_x_array, subarea_y_array = self.find_subareas(x, y)
        for xt in subarea_x_array:
            for yt in subarea_y_array:
                if modified_table[xt][yt] != 0:
                    count += 1
        return count

    @staticmethod
    def find_subareas(x, y):
        for xt in range(3):
            for yt in range(3):
                subarea_x_array = [xt*3+x_ar for x_ar in range(3)]
                subarea_y_array = [yt*3+y_ar for y_ar in range(3)]
                if x in subarea_x_array and y in subarea_y_array:
                    return subarea_x_array, subarea_y_array


class TestingSudoku(CreateSudoku):

    def test_table(self, origin_table):
        modified_table = origin_table
        for num in range(1, 10):
            error = self.check_line_for_repeat_numbers(modified_table, num) or \
                    self.check_column_for_repeat_numbers(modified_table, num) or \
                    self.check_areas_for_repeat_numbers(modified_table, num)
            print(str(num) + ":" + str(error))

    @staticmethod
    def check_line_for_repeat_numbers(origin_table, num):
        for x in range(len(origin_table)):
            if origin_table[x].count(num) > 1:
                return True
        return False

    def check_column_for_repeat_numbers(self, origin_table, num):
        modified_table = origin_table
        self.mirror_reverse(modified_table)
        error = self.check_line_for_repeat_numbers(modified_table, num)
        self.mirror_reverse(modified_table)
        return error

    def check_areas_for_repeat_numbers(self, origin_table, num):
        modified_table = origin_table
        for x in range(3):
            for y in range(3):
                error = self.check_area_for_repeat_numbers(modified_table, num, x, y)
                if error:
                    return True
        return False

    @staticmethod
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

# Main Part

if __name__ == '__main__':
    new_sudoku = CreateSudoku()
    new_print = PrintSudoku()
    new_test = TestingSudoku()
    new_table = new_sudoku.make_random_table(ORIGIN_TEMPLATE_TABLE)
    # For test (False eq "All Right", True eq "Something Wrong"):
    # new_test.test_table(new_table)
    # PrintSudoku.print_table(new_table)
    new_print.print_table_secret(new_table, DIFFICULT['1'])


################################################################################
################################################################################
#                          Solving puzzle area                                 #
################################################################################
################################################################################


# TODO: solving puzzle class
