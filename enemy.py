from ship import Ship

class Enemy(Ship):
    def __init__(self, image, size, start_pos, speed) -> None:
        super().__init__(image, size, start_pos, speed)