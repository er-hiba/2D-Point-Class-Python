class Point():
    def __init__(self, x_coordinate=0, y_coordinate=0):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.__y_coordinate = y_coordinate

    def distance(self, other_point):
        x = other_point.get_x_coordinate()
        y = other_point.get_y_coordinate()
        a = self.get_x_coordinate()
        b = self.get_y_coordinate()

        distance = ((a - x) ** 2 + (b - y) ** 2) ** 0.5

        return distance

    def norm(self):
        a = self.get_x_coordinate()
        b = self.get_y_coordinate()

        distance = (a ** 2 + b ** 2) ** 0.5

        return distance
