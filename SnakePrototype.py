import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Snake:
    def __init__(self, coordinates, direction, color):
        self.coordinates = coordinates
        self.direction = direction
        self.color = color
        print("Created Snake")

    def __copy__(self):
        coordinates = copy.copy(self.coordinates)
        new = self.__class__(
            coordinates, self.direction, self.color
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        coordinates = copy.deepcopy(self.coordinates, memo)
        new = self.__class__(
            coordinates, self.direction, self.color
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":
    snake = Snake((1, 1), 1, "red")
    snake2 = copy.copy(snake)
    