class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, W):
        self.width = W

    def set_height(self, H):
        self.height = H

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            pic = ""
            for i in range(self.height):
                pic += self.width * '*' + '\n'
            return pic

    def get_amount_inside(self, shape):
        count = 0
        h = 0
        w = 0
        if self.height >= shape.height:
            h = self.height // shape.height
        if self.width >= shape.width:
            w = self.width // shape.width

        count = h * w
        return count


class Square(Rectangle):

    def __init__(self, side, width, height):
        super().__init__(width, height)
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, S):
        self.height = S
        self.width = S
