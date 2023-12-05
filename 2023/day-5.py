from collections import defaultdict


maps = [
    'seed-to-soil map:',
    'soil-to-fertilizer map:',
    'fertilizer-to-water map:',
    'water-to-light map:',
    'light-to-temperature map:',
    'temperature-to-humidity map:',
    'humidity-to-location map:',
    ]


def create_mappings(data):
    mappings = defaultdict(list)
    curr_map = ''

    for i in range(len(data)):
        if data[i] in maps:
            curr_map = data[i]
        else:
            nums = [int(_) for _ in data[i].split(' ')]
            mappings[curr_map].append(nums)
    
    return mappings


# Part one
def low_loc(data):
    seeds = [int(_) for _ in data[0].split(':')[1].strip().split(' ')]
    data = data[1:]
    mappings = create_mappings(data)

    locations = []
    for seed in seeds:
        s = seed
        for m in maps:
            for r in mappings[m]:
                if s >= r[1] and s <= (r[1] + r[2])-1:
                    s = (s - r[1]) + r[0]
                    break
        locations.append(s)
    print('Part one:', min(locations))


def dnc(start, end, mappings, map, entry):
    if map > len(maps)-1:
        return start
    if entry > len(mappings[maps[map]])-1:
        if maps[map] == 'humidity-to-location map:':
            return start
        return dnc(start, end, mappings, map+1, 0)
    else:
        src = mappings[maps[map]][entry][1]
        dest = mappings[maps[map]][entry][0]
        range = mappings[maps[map]][entry][2]

        # Start and end are beyond the range
        if start < src and end > src+range-1:
            return min(
                dnc(start, src-1, mappings, map, entry+1),
                dnc(dest, (dest+range)-1, mappings, map+1, 0),
                dnc(src+range, end, mappings, map, entry+1)
            )
        # Start is beyond the range
        elif start < src and end <= src+range-1:
            return min(
                dnc(start, src-1, mappings, map, entry+1),
                dnc(dest, dest+(range-((src+range-1)-end-1)), mappings, map+1, 0)
            )
        # End is beyond the range
        elif start >= src and end > src+range-1:
            return min(
                dnc(src+range, end, mappings, map, entry+1),
                dnc(dest+(start-src), dest+range-1, mappings, map+1, 0)
            )
        # If start and end are within the range
        elif start >= src and end <= src+range-1:
            return dnc(
                dest+(start-src),
                dest+(range-((src+range-1)-end-1)),
                mappings, map+1, 0
                )
        # If not within the range at all
        else:
            return dnc(start, end, mappings, map, entry+1)


# Part two
def eff_low_loc(data):
    seeds = [int(_) for _ in data[0].split(':')[1].strip().split(' ')]
    seed_ranges = {seeds[i]: seeds[i]+seeds[i+1]-1 for i in range(0, len(seeds)-1, 2)}
    data = data[1:]
    mappings = create_mappings(data)

    locations = []
    for start,end in seed_ranges.items():
        locations.append(dnc(start, end, mappings, 0, 0))

    print('Part two:', min(locations))


def main():
    with open('inputs/test.in', 'r') as file:
        data = [line for line in file.read().strip().split('\n') if line != '']
    low_loc(data)
    eff_low_loc(data)


if __name__ == '__main__':
    main()