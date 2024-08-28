from ship import Ship

class Player(Ship):
    def __init__(self, image, size, start_pos) -> None:
        super().__init__(image, size, start_pos)