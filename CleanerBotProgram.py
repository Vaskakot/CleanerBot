width = 7
height = 7
up = [0, -1]
down = [0, 1]
right = [1, 0]
left = [-1, 0]
directions = [up, right, down, left]


class Robot:
    def __init__(self, a, b, direction, field):
        self.coord = [a, b]
        self.dir = direction
        self.field = field

    def move(self):
        self.coord[0] = self.coord[0] + directions[self.dir][0]
        self.coord[1] = self.coord[1] + directions[self.dir][1]

    def turn_left(self):
        self.dir = (self.dir - 1) % len(directions)

    def turn_right(self):
        self.dir = (self.dir + 1) % len(directions)

    def is_free(self):
        if self.field[self.coord[0] + directions[self.dir][0]][self.coord[1] + directions[self.dir][1]] != -1:
            return True
        else:
            return False

    def is_free_left(self):
        # TODO: исправить self.dir +- 1 - на деление по модулю иначе будет ошибка
        if self.field[self.coord[0] + directions[self.dir - 1][0]][self.coord[1] + directions[self.dir - 1][1]] != -1:
            return True
        else:
            return False

    def is_free_right(self):
        if self.field[self.coord[0] + directions[self.dir + 1][0]][self.coord[1] + directions[self.dir + 1][1]] != -1:
            return True
        else:
            return False

    def is_wall(self):
        if self.field[self.coord[0] + directions[self.dir][0]][self.coord[1] + directions[self.dir][1]] == -1:
            return True
        else:
            return False

    def is_wall_left(self):
        if self.field[self.coord[0] + directions[self.dir - 1][0]][self.coord[1] + directions[self.dir - 1][1]] == -1:
            return True
        else:
            return False

    def is_wall_right(self):
        if self.field[self.coord[0] + directions[self.dir + 1][0]][self.coord[1] + directions[self.dir + 1][1]] == -1:
            return True
        else:
            return False

    def is_cleaned(self):
        if self.field[self.coord[0] + directions[self.dir][0]][self.coord[1] + directions[self.dir][1]] == 0:
            return True
        else:
            return False

    def is_cleaned_left(self):
        if self.field[self.coord[0] + directions[self.dir - 1][0]][self.coord[1] + directions[self.dir - 1][1]] == 0:
            return True
        else:
            return False

    def is_cleaned_right(self):
        if self.field[self.coord[0] + directions[self.dir + 1][0]][self.coord[1] + directions[self.dir + 1][1]] == 0:
            return True
        else:
            return False

    def is_dirty(self):
        if self.field[self.coord[0] + directions[self.dir][0]][self.coord[1] + directions[self.dir][1]] == 1:
            return True
        else:
            return False

    def is_dirty_left(self):
        if self.field[self.coord[0] + directions[self.dir - 1][0]][self.coord[1] + directions[self.dir - 1][1]] == 1:
            return True
        else:
            return False

    def is_dirty_right(self):
        if self.field[self.coord[0] + directions[self.dir + 1][0]][self.coord[1] + directions[self.dir + 1][1]] == 1:
            return True
        else:
            return False


def make_field(width, height):
    field = [[1 for x in range(width)] for y in range(height)]
    field[1][1] = 2
    for x in range(width):
        field[x][0] = -1
        field[x][height - 1] = -1
    for y in range(height):
        field[0][y] = -1
        field[width - 1][y] = -1
    return field


def print_field(field):
    for y in range(height):
        for x in range(width):
            print('{0:2d}'.format(field[x][y]), end=" ")
        print()


if __name__ == "__main__":
    print_field(run_me(width, height))