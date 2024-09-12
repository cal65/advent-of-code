from day2 import read_file

def parse_soil_text(d5):
    maps_raw = {}
    add = False
    for i in range(1, len(d5)):
        if re.search('^[A-Za-z]', d5[i]):
            t = d5[i]
            label = t.replace(' map:', '')
            maps_raw[label] = []
            add = True
        else:
            if label in maps_raw.keys():
                nums = d5[i].split(' ')
                nums = [int(n) for n in nums]
                maps_raw[label].append(nums)
    return maps_raw


def retrieve(s, value):
    source_min = s[1]
    source_max = s[1] + s[2]
    dest_min = s[0]
    if value>= source_min and value <source_max:
        return dest_min + value - source_min
    else:
        return value


def parse_seeds_one(d5):
    seeds = d5[0].split('seeds: ')[1]
    seeds = [int(s) for s in seeds.split(' ')]
    return seeds


def d5_part1(seeds):
    solutions = []
    for d in seeds:
        for name in map_names:
            for s in soil_mapper_raw[name]:
                d_new = retrieve(s, d)
                if d_new!=d:
                    d = d_new
                    break
        solutions.append(d)
    return solutions


def parse_seeds_two(d5):
    seeds = parse_seeds_one(d5)
    range_extents = []
    half_len = int(len(seeds)/2)
    for i in range(half_len):
        s = seeds[i:i+2]
        range_extents.append((s[0], s[0] + s[1]))
    return range_extents


def split_and_modify_range(r, min_value, max_value, modify_by):
    # we pass in r. The min and max comes from the dictionary
    # if we have a range 97, 98, 99 and dictionary includes 98 and 99, we want 97 to not get mapped
    mapped_ranges = set()
    unmapped_ranges = set()
    # Get the start and stop of the range
    r_start, r_stop = r.start, r.stop

    # Handle the range below the min_value
    if r_start < min_value:
        unmapped_ranges.add(range(r_start, min(min_value, r_stop)))

    # Handle the range between min_value and max_value
    if min_value < r_stop and r_start < max_value:
        mapped_ranges.add(range(max(r_start, min_value) + modify_by, min(r_stop, max_value) + modify_by))

    # Handle the range above max_value
    if r_stop > max_value:
        unmapped_ranges.add(range(max(r_start, max_value), r_stop))


    return mapped_ranges, unmapped_ranges

def map_range(s, r):
    return split_and_modify_range(r, s[1], s[1] + s[2] + 1, s[0] - s[1])


def map_range_set(s, ranges):
    new_ranges_mapped = set()
    new_ranges_unmapped = set()
    for r in ranges:
        mapped, unmapped = split_and_modify_range(r, s[1], s[1] + s[2] + 1, s[0] - s[1])
        new_ranges_mapped.update(mapped)
        new_ranges_unmapped.update(unmapped)
    return new_ranges_mapped, new_ranges_unmapped



def iterate_ranges(ranges, m):
    for name in m:
        mapped_ranges = set()
        unmapped_ranges = set()
        
        for s in m[name]:
            # get what was mapped and what wasn't
            new_range_mapped, new_range_unmapped = map_range_set(s, ranges)
            # if something was mapped
            if new_range_mapped:
                # keep track of what was mapped
                mapped_ranges.update(new_range_mapped)
                # set ranges to only the remaining unmapped
                ranges = new_range_unmapped
        # update ranges to get back the mapped parts for the next dictionary
        ranges.update(mapped_ranges)        
    
    return ranges

            


if __name__ == '__main__':
	d5 = read_file('day5.txt')


