CELL_WALL = -1  # так обозначается стена
CELL_CLEAN = 0  # так обозначается убранная клетка
CELL_DIRTY = 1  # так обозначается неубранная клетка
CELL_BASE = 2  # так обозначается подзарядка
width = 12
height = 8
up = [0, -1]
down = [0, 1]
right = [1, 0]
left = [-1, 0]
directions = [up, right, down, left]


class Robot:
    def __init__(self, a, b, direction, field):
        self.coord = [a, b]  # первоначальные координаты робота
        self.dir = direction  # указатель направления в массиве directions
        self.field = field  # поле нашей комнаты

    def move(self):
        if self.field[self.coord[0]][self.coord[1]] == CELL_DIRTY:
            field[self.coord[0]][self.coord[1]] = CELL_CLEAN
        if self.is_free():
            self.coord[0] = self.coord[0] + directions[self.dir][0]
            self.coord[1] = self.coord[1] + directions[self.dir][1]

    def turn_left(self):
        self.dir = (self.dir - 1) % len(directions)

    def turn_right(self):
        self.dir = (self.dir + 1) % len(directions)

    def look_left(self):
        return (self.dir - 1) % len(directions)

    def look_right(self):
        return (self.dir + 1) % len(directions)

    def cell_at_left(self):
        dir_ = self.direction_left()
        return self.field[self.coord[0] + dir_[0]][self.coord[1] + dir_[1]]

    def cell_at_right(self):
        dir_ = self.direction_right()
        return self.field[self.coord[0] + dir_[0]][self.coord[1] + dir_[1]]

    def cell_front(self):
        dir_ = directions[self.dir]
        return self.field[self.coord[0] + dir_[0]][self.coord[1] + dir_[1]]

    def direction_left(self):
        return directions[self.look_left()]

    def direction_right(self):
        return directions[self.look_right()]

    def is_free(self):
        if self.cell_front() != CELL_WALL:
            return True
        else:
            return False

    def is_free_left(self):
        if self.cell_at_left() != CELL_WALL:
            return True
        else:
            return False

    def is_free_right(self):
        if self.cell_at_right() != CELL_WALL:
            return True
        else:
            return False

    def is_wall(self):
        if self.cell_front() == CELL_WALL:
            return True
        else:
            return False

    def is_wall_left(self):
        if self.cell_at_left() == CELL_WALL:
            return True
        else:
            return False

    def is_wall_right(self):
        if self.cell_at_right() == CELL_WALL:
            return True
        else:
            return False

    def is_cleaned(self):
        if self.cell_front() == CELL_CLEAN:
            return True
        else:
            return False

    def is_cleaned_left(self):
        if self.cell_at_left() == CELL_CLEAN:
            return True
        else:
            return False

    def is_cleaned_right(self):
        if self.cell_at_right() == CELL_CLEAN:
            return True
        else:
            return False

    def is_dirty(self):
        if self.cell_front() == CELL_DIRTY:
            return True
        else:
            return False

    def is_dirty_left(self):
        if self.cell_at_left() == CELL_DIRTY:
            return True
        else:
            return False

    def is_dirty_right(self):
        if self.cell_at_right() == CELL_DIRTY:
            return True
        else:
            return False


def make_field(width, height):
    field = [[1 for y in range(height)] for x in range(width)]
    field[1][1] = 2
    for x in range(width):
        field[x][0] = -1
        field[x][height - 1] = -1
    for y in range(height):
        field[0][y] = -1
        field[width - 1][y] = -1
    return field


def print_field(field):
    print()
    for y in range(height):
        for x in range(width):
            print('{0:2d}'.format(field[x][y]), end=" ")
        print()


def clean_room(robot):
    while robot.is_free():
        robot.move()
    robot.turn_right()
    while robot.is_free():
        robot.move()
    while robot.is_free_right():
        print_field(robot.field)
        robot.turn_right()
        robot.move()
        robot.turn_right()
        while robot.is_dirty():
            robot.move()
        robot.turn_left()
        robot.move()
        robot.turn_left()
        while robot.is_free():
            robot.move()
    while robot.is_free():
        robot.move()
    robot.turn_left()
    robot.turn_left()
    while robot.is_free():
        robot.move()


if __name__ == "__main__":
    field = make_field(width, height)
    robot = Robot(1, 1, 1, field)
    print_field(field)
    clean_room(robot)
    print_field(field)
