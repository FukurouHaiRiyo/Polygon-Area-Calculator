class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return self.width ** 2 + self.height ** 2

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Picture too big'
        
        line = '*' * self.width # number of '*' in each line
        lines = [line for _ in range(self.height)] # number of lines in shape

        pic = '\n'.join(lines)

        return pic + '\n'

    def get_amount_inside(self, shape):
        shape = Rectangle
        w = self.width // shape.width
        h = self.height // shape.height

        return w*h

    def __str__(self):
        return f'Rectangle dimensions:\n Width: {self.width}\n Height: {self.height}'


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square dimensions:\n Side; {self.width}'
