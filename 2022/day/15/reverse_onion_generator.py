import unittest

def generate_reverse_onion(max_coord):
    layer = 0
    while layer < max_coord//2 + 1:
        layer_min = int(max_coord/2-max_coord%2/2)-layer
        layer_max = int(max_coord/2+max_coord%2/2)+layer
        if layer_min == layer_max:
            yield (layer_min,layer_min)
        else:
            for position in [(x,layer_min) for x in range(layer_min,layer_max+1)]:
                yield position
            for row in range(layer_min+1,layer_max):
                for position in [(layer_min,row),(layer_max,row)]:
                    yield position
            for position in [(x,layer_max) for x in range(layer_min,layer_max+1)]:
                yield position
        layer += 1

class TestOnionGenerator(unittest.TestCase):

    test_values = [
        (
            0,
            [(0,0)],
        ),
        (
            1,
            [(0,0),(1,0),(0,1),(1,1)],
        ),
        (
            2,
            [(1,1),(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2)]
        ),
        (   3,
            [(1,1),(2,1),(1,2),(2,2),(0,0),(1,0),(2,0),(3,0),(0,1),(3,1),(0,2),(3,2),(0,3),(1,3),(2,3),(3,3)]
        ),
        ]

    def test(self):
        for test_case in self.test_values:
            with self.subTest('Test {}x{}'.format(test_case[0],test_case[0])):
                self.assertEqual([x for x in generate_reverse_onion(test_case[0])],test_case[1])