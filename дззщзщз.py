class Tree_Seeds:
    def about(self):
        print('I am Tree Seeds')
    def about_myself(self):
        print('I am Tree Seeds')
class Apple_Tree(Tree_Seeds):
    def about_myself(self):
        print('I am Apple Tree')
class Apple(Apple_Tree):
    height = 3
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

class Apple(Fruit):
    def __init__(self):
        super().about()
        super().about_myself()