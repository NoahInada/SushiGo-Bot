__author__ = 'Noah'
class Cordinates:
    onHandFoodCords = {
        'shrimp': (35, 333),
        'rice': (92, 338),
        'nori': (35, 392),
        'roe': (89, 392),
        'salmon': (42, 446),
        'unagi': (111, 812)
    }

    plates = [(81, 203), (182, 204), (284, 210), (383, 203), (485, 207), (587, 203)]

    phone = (581, 364)

    topping_menu = (546, 273)
    exit_menu = (585, 338)

    rice_menu = (546, 295)
    m_rice = (546, 283)

    toBuyFoodCords = {
        'shrimp': (524, 225),
        'unagi': (601, 225),
        'nori': (520, 280),
        'roe': (602, 280),
        'salmon': (519, 335),
    }

    normal_delivery = (493, 293)


class AllColors:
    no_roe = (109, 123, 127)
    no_rice = (127, 127, 127)
    sushiGS = {
        1961: 'caliroll',
        1843: 'onigiri',
        1573: 'gunkan'
    }

    '''
    desktop:
    2100: 'caliroll',
    1843: 'onigiri',
    1770: 'gunkan'

    laptop:
    1961 : 'caliroll',
    1843 : 'onigiri',
    1573 : 'gunkan'



    '''




    blankGS = {
        'seat1': 5514,
        'seat2': 4792,
        'seat3': 9335,
        'seat4': 9254,
        'seat5': 4948,
        'seat6': 7038
    }

class Recipes:
    Cords = Cordinates
    foods = {
        'caliroll':{'roe': 1, 'nori': 1, 'rice': 1},
        'onigiri':{'rice': 2, 'nori': 1},
        'gunkan':{'rice': 1, 'nori': 1, 'roe': 2}
    }