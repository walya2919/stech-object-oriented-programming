class Foo:
    def __init__(self):
        print('foo')

class Bar(Foo):
    def __init__(self):
        print('bar')
        super.__init__()

bar = Bar()

"""
super.__init__()을 실행시키면, super라는 함수 객체에서 __init__속성을
찾으려 하기 때문에, TypeError가 발생한다.

"""