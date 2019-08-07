class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    p = Point(3,5)
    print(f"х = {p.x}, y = {p.y}")

if __name__ == main:
    main()
