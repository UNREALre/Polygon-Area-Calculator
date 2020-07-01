class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if type(self).__name__ == 'Square':
            str = '{}(side={})'.format(type(self).__name__, self.width, self.height)
        else:
            str = '{}(width={}, height={})'.format(type(self).__name__, self.width, self.height)

        return str

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append('*')
            pic.append(''.join(row))

        return '\n'.join(pic)+'\n'

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)
