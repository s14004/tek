class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def say(self):
        print(self.voice)


class Dog(Animal):
    pass

if __name__ == '__main__':
    puppy = Dog(name='shima', voice='nyan!')
    puppy.say()