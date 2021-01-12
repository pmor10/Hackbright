"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for name, attr in melons.items():
        print(name.upper())

        for att, value in attr.items():
            print(f'{att} : {value}')
        print('--------------------')

print_melon(melons)