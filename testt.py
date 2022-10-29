    def __init__(self, name):
        self.name = name
        self.alive = True
        self.progress = 0
        self.gladness = 50
        self.money = 1000
        self.truant = 0
        self.gladness1 = 7

    def to_work(self):
        print('Go to work')
        self.money += 300
        self.gladness1 -= 100

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
    def to_chill(self):
        print('Rest time')
        self.progress -= 0.1
        self.gladness += 5

    def is_gotowork(self):
        if self.money < +700:
            print('You have 3 days weekend')
            self.money = True
        elif self.truant <= 5:
            print('you are fired')
            self.truant = False
        elif self.progress > 5:
            print('Go to new work')
            self.to_work()


    # OOP
    import random


    class Student:
        def __init__(self, name):
            self.name = name
            self.alive = True
            self.progress = 0
            self.gladness = 50
            self.money = 1000
            self.truant = 0
            self.gladness1 = 7

        def to_work(self):
            print('Go to work')
            self.money += 300
            self.gladness1 -= 100

        def to_study(self):
            print('Time to study')
            self.progress += 0.12
            self.gladness -= 3

        def to_sleep(self):
            print('I will sleep')
            self.gladness += 3

        def to_chill(self):
            print('Rest time')
            self.progress -= 0.1
            self.gladness += 5

        def is_gotowork(self):
            if self.money < +700:
                print('You have 3 days weekend')
                self.money = True
            elif self.truant <= 5:
                print('you are fired')
                self.truant = False
            elif self.progress > 5:
                print('Go to new work')
                self.to_work()

        def is_alive(self):
            if self.progress < -0.5:
                print('Cast out...')
                self.alive = False
            elif self.gladness <= 0:
                print('Depression')
                self.alive = False
            elif self.progress > 5:
                print('Passed externally...')
                self.alive = False

        def end_of_day(self):
            print(f'Glagness = {self.gladness}')
            print(f'Progress = {round(self.progress, 2)}')

        def live(self, day):
            day = 'Day ' + str(day) + ' of ' + self.name + ' live'
            print(f"{day:=^50}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            self.end_of_day()
            self.is_alive()


    nick = Student(name='Nick')

    for day in range(365):
        if nick.alive == False:
            break
        nick.live(day)
