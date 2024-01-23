from plur import plur


def test_simple():
    assert plur('dog')(0) == '0 dogs'
    assert plur('dog')(1) == '1 dog'
    assert plur('dog')(2) == '2 dogs'


def test_ending():
    assert plur('ox', '-en')(0) == '0 oxen'
    assert plur('ox', '-en')(1) == '1 ox'
    assert plur('ox', '-en')(2) == '2 oxen'


def test_defered():
    dog = plur('dog', zero='doggoes')

    assert dog(0) == '0 doggoes'
    assert dog(1) == '1 dog'
    assert dog(2) == '2 dogs'
    assert dog(3) == '3 dogs'
    assert dog(4) == '4 dogs'


def test_exotic():
    dog = plur('dog', '-s', '-s', 'pups', zero='doggoes', num_first=False, sep=': ')

    assert dog(0) == 'doggoes: 0'
    assert dog(1) == 'dog: 1'
    assert dog(2) == 'dogs: 2'
    assert dog(3) == 'dogs: 3'
    assert dog(4) == 'pups: 4'
    assert dog(5) == 'pups: 5'
