class Glass:
    capacity = 250

    def __init__(self, content=0):
        self.content = content

    def fill(self, ml):
        if self.capacity >= self.content + ml:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        space_left = self.capacity - self.content
        if space_left:
            return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
