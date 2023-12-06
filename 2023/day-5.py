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


def dnc_intervals(start, end, mappings, map, entry):
    if map > len(maps)-1:
        return start
    if entry > len(mappings[maps[map]])-1:
        if maps[map] == 'humidity-to-location map:':
            return start
        return dnc_intervals(start, end, mappings, map+1, 0)
    
    src_start = mappings[maps[map]][entry][1]
    dest_start = mappings[maps[map]][entry][0]
    range = mappings[maps[map]][entry][2]

    # If interval overlaps src interval
    if start < src_start and end >= src_start + range:
        return min(
            dnc_intervals(start, src_start-1, mappings, map, entry+1),
            dnc_intervals(dest_start, dest_start+range-1, mappings, map+1, 0),
            dnc_intervals(src_start + range, end, mappings, map, entry+1)
        )
    # If interval start is less than src start
    elif start < src_start and end < src_start + range and end >= src_start:
        return min(
            dnc_intervals(start, src_start-1, mappings, map, entry+1),
            dnc_intervals(dest_start, dest_start+range-((src_start+range-1)-end)-1, mappings, map+1, 0)
        )
    # If interval end is greater than src end
    elif start >= src_start and start < src_start+range and end >= src_start+range:
        return min(
            dnc_intervals(src_start+range, end, mappings, map, entry+1),
            dnc_intervals(dest_start+(start-src_start), dest_start+range-1, mappings, map+1, 0)
        )
    # If interval within src interval
    elif start >= src_start and end < src_start+range:
        return dnc_intervals(
            dest_start+(start-src_start),
            dest_start+range-((src_start+range-1)-end)-1,
            mappings, map+1, 0
        )
    else:
        return dnc_intervals(start, end, mappings, map, entry+1)


# Part two
def eff_low_loc(data):
    seeds = [int(_) for _ in data[0].split(':')[1].strip().split(' ')]
    seed_ranges = {seeds[i]: seeds[i]+seeds[i+1]-1 for i in range(0, len(seeds)-1, 2)}
    data = data[1:]
    mappings = create_mappings(data)
    locations = []
    for start,end in seed_ranges.items():
        locations.append(dnc_intervals(start, end, mappings, 0, 0))
    print('Part two:', min(locations))


def main():
    with open('inputs/day-5.in', 'r') as file:
        data = [line for line in file.read().strip().split('\n') if line != '']
    low_loc(data)
    eff_low_loc(data)


if __name__ == '__main__':
    main()