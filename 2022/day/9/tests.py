import unittest
import solver

class TestSolver(unittest.TestCase):

    move_cases = [
        # (initial_state, move, output_state)
        (
            ['......',
             '......',
             '......',
             '......',
             'H.....'],
            'R 4',
            ['......',
             '......',
             '......',
             '......',
             's..TH.'],
        ),
        (
            ['......',
             '......',
             '......',
             '......',
             's..TH.'],
            'U 4',
            ['....H.',
             '....T.',
             '......',
             '......',
             's.....'],
        ),
        (
            ['....H.',
             '....T.',
             '......',
             '......',
             's.....'],
            'L 3',
            ['.HT...',
             '......',
             '......',
             '......',
             's.....'],
        ),
        (
            ['.HT...',
             '......',
             '......',
             '......',
             's.....'],
            'D 1',
            ['..T...',
             '.H....',
             '......',
             '......',
             's.....'],
        ),
        (
            ['..T...',
             '.H....',
             '......',
             '......',
             's.....'],
            'R 4',
            ['......',
             '....TH',
             '......',
             '......',
             's.....'],
        ),
        (
            ['......',
             '....TH',
             '......',
             '......',
             's.....'],
            'D 1',
            ['......',
             '....T.',
             '.....H',
             '......',
             's.....'],
        ),
        (
            ['......',
             '....T.',
             '.....H',
             '......',
             's.....'],
            'L 5',
            ['......',
             '......',
             'HT....',
             '......',
             's.....'],
        ),
        (
            ['......',
             '......',
             'HT....',
             '......',
             's.....'],
            'R 2',
            ['......',
             '......',
             '.TH...',
             '......',
             's.....'],
        ),
    ]
    tail_update_cases = [
        (
            ['.H',
             '..',
             'T.'],
            ['.H',
             '.T',
             '..']
        ),
        (
            ['H.',
             '..',
             '.T'],
            ['H.',
             'T.',
             '..']
        ),
        (
            ['.T',
             '..',
             'H.'],
            ['..',
             'T.',
             'H.']
        ),
        (
            ['T.',
             '..',
             ' H'],
            ['..',
             '.T',
             '.H']
        ),
        (
            ['H..',
             '..T'],
            ['HT.',
             '...']
        ),
        (
            ['..H',
             'T..'],
            ['.TH',
             '...']
        ),
        (
            ['..T',
             'H..'],
            ['...',
             'HT.']
        ),
        (
            ['T..',
             '..H'],
            ['...',
             '.TH']
        ),
        (
            ['H..',
             '..T'],
            ['HT.',
             '...']
        ),
        (
            ['H.T'],
            ['HT.']
        ),
        (
            ['T.H'],
            ['.TH']
        ),
        (
            ['H',
             '.',
             'T'],
            ['H',
             'T',
             '.']
        ),
        (
            ['T',
             '.',
             'H'],
            ['.',
             'T',
             'H']
        ),
    ]
    visited_case = (
        # moves
        ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2'],
        # visited
        ['..##..',
         '...##.',
         '.####.',
         '....#.',
         's###..'],
        # visited count
        13
    )

    def test_moves(self):
        for state_before, move_descriptor, state_after in self.move_cases:
            with self.subTest(msg=move_descriptor):
                positions_before = decode_state(state_before)
                positions_after = decode_state(state_after)
                move_direction, move_count = move_descriptor.split()
                rope_bridge = solver.RopeBridge(positions_before)
                for _ in range(int(move_count)):
                    rope_bridge.move_head(move_direction)
                    rope_bridge.update_tails()
                self.assertEqual(tuple(rope_bridge.positions[0]), positions_after[0])
                self.assertEqual(tuple(rope_bridge.positions[1]), positions_after[1])

    def test_tail_update(self):
        for state_before, state_after in self.tail_update_cases:
            with self.subTest(state_before):
                rope_bridge = solver.RopeBridge(decode_state(state_before))
                rope_bridge.update_tails()
                head_after, tail_after = decode_state(state_after)
                self.assertEqual(tuple(rope_bridge.positions[0]), head_after)
                self.assertEqual(tuple(rope_bridge.positions[1]), tail_after)



    def test_visited(self):
        visited_positions = set()
        rope_bridge = solver.RopeBridge()
        for move_descriptor in self.visited_case[0]:
            move_direction, move_count = move_descriptor.split()
            for _ in range(int(move_count)):
                rope_bridge.move_head(move_direction)
                rope_bridge.update_tails()
                visited_positions.add(tuple(rope_bridge.positions[1]))
        expected_visited = decode_visited(self.visited_case[1])
        self.assertSetEqual(visited_positions, expected_visited)
        self.assertEqual(len(visited_positions), self.visited_case[2])

def decode_state(state):
    '''convert a state map to head and tail positions'''
    head = None
    tail = None
    for y, line in enumerate(reversed(state)):
        for x, position in enumerate(line):
            if position == 'H':
                head = (x,y)
            if position == 'T':
                tail = (x,y)
    if not head:
        raise RuntimeError('Head not found in state.')
    tail = tail or tuple(head)
    return head, tail

def decode_visited(visited):
    '''Decode a map of visited positions'''
    visited_positions = set()
    for y, line in enumerate(reversed(visited)):
        for x, position in enumerate(line):
            if position == '#' or position == 's':
                visited_positions.add((x,y))
    return visited_positions
