from collections.abc import Iterable, Generator


def read_terminal_output(terminal_output: Iterable[str]) -> Iterable[list[str]]:
    data = None
    for line in terminal_output:
        line = line.strip()
        if line.startswith('$'):
            if data:
                yield data
            data = [line]
        else:
            data.append(line)
    yield data

def populate_filesystem(terminal_output_gen: Iterable, filesystem_structure: dict):
    #for terminal_output in terminal_output_gen:
    terminal_output = next(terminal_output_gen)
    while terminal_output:
        if terminal_output[0] == '$ cd /':
            raise RuntimeError('"$ cd /" encountered unexpectedly.')
        elif terminal_output[0] == '$ cd ..':
            return
        elif terminal_output[0] == '$ ls':
            #   process listing, creating file and directory entries
            for listing in terminal_output[1:]:
                listing = listing.strip('\n').split()
                if listing[0] == 'dir':
                    # create directory child
                    filesystem_structure['children'].append({'name': listing[1], 'type': 'dir', 'children': [],})
                else:
                    # create file child
                    filesystem_structure['children'].append({'name': listing[1], 'type': 'file', 'size': int(listing[0])})
        elif terminal_output[0].startswith('$ cd'):
            directory_name = terminal_output[0].split()[2]
            for child in filesystem_structure['children']:
                if child['name'] == directory_name:
                    populate_filesystem(terminal_output_gen,child)
                    break
        try:
            terminal_output = next(terminal_output_gen)
        except StopIteration:
            return

def calculate_directory_sizes(filesystem_structure, directories) -> int:
    directory_size = 0
    for child in filesystem_structure['children']:
        if child['type'] == 'dir':
            directory_size += calculate_directory_sizes(child, directories)
        if child['type'] == 'file':
            directory_size += child['size']
    directories.append((directory_size,filesystem_structure['name']))
    return directory_size

def print_directory(filesystem_structure, indent):
    print('{}- {} ({})'.format(' '*indent, filesystem_structure['name'], filesystem_structure['type']))
    for child in filesystem_structure['children']:
        if child['type'] == 'dir':
            print_directory(child, indent + 2)
        else:
            print('{}  - {} ({}, size={})'.format(' '*indent, child['name'], child['type'], child['size']))

def part1(terminal_output):
    filesystem_structure = {'name': '/', 'type': 'dir', 'children': []}
    terminal_output_gen = iter(read_terminal_output(terminal_output))
    if next(terminal_output_gen)[0] != '$ cd /':
        raise RuntimeError('"$ cd /" not at start of terminal output.')
    populate_filesystem(terminal_output_gen, filesystem_structure)
    print_directory(filesystem_structure, 0)
    directories = []
    calculate_directory_sizes(filesystem_structure, directories)
    return sum([size for size,name in directories if size <= 100000])


def part2(terminal_output):
    filesystem_structure = {'name': '/', 'type': 'dir', 'children': []}
    terminal_output_gen = iter(read_terminal_output(terminal_output))
    if next(terminal_output_gen)[0] != '$ cd /':
        raise RuntimeError('"$ cd /" not at start of terminal output.')
    populate_filesystem(terminal_output_gen, filesystem_structure)
    directories = []
    used_space = calculate_directory_sizes(filesystem_structure, directories)
    print('Used Space: {}'.format(used_space))
    target_to_delete = used_space - 40000000
    to_delete = 70000000
    for directory in directories:
        if target_to_delete <= directory[0] and directory[0] < to_delete:
            to_delete = directory[0]
    return to_delete

    

if __name__ == '__main__':
    with open('input', 'r') as input_data:
        print(part1(input_data))
    with open('input', 'r') as input_data:
        print(part2(input_data))
