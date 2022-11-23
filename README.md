# plur: 🔢 simple universal word pluralizer 🔢

Tired of seeing `1 branch(es) deleted`?

Sick of

    es = '' if len(branches) == 1 else 'es'
    print(f'{len(branches) branch{es} created')

or even worse?

Try `plur` for your tiny pluralization needs:

    import plur

    print(plur('branch', '-es'), branches), 'created)

* No dictionary file!
* No dependencies!
* No salesperson will call!

Examples:

    import plur

    dogs = ['fido', 'rover']
    print(plur('dog', dogs))  # prints: 2 dogs

    dogs.pop()
    print(plur('dog', dogs))  # prints: 1 dog

    dogs.pop()
    print(plur('dog', dogs))  # prints: 0 dogs

    # Great for f-strings

    dogs = 'fido', 'rover'
    print(f'Today we have {plur("dog", dogs)}')

For words you use a lot, you can defer operation:

    dog = plur('dog')
    cat = plur('cat')
    ox = plur('ox', '-en')

    print(dog(dogs), 'live in my house with', ox(ox_list))
