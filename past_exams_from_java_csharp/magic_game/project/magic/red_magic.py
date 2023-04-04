from project.magic.magic import Magic


class RedMagic(Magic):
    def __init__(self, name, bullets_count):
        super().__init__(name, bullets_count)
        self.bullets = self.bullets_count()

    def fire(self):
        if self.bullets - 1 < 0:
            self.bullets = 0
            return 0
        else:
            self.bullets -= 1
            return 1