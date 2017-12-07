# 
# Given a graph in which every node (tower) has a weight.
# The weights of the towers should sum up equally.
# There is one tower which weight is wrong, find the tower, which weight should it have?
# More detailed description:
# http://adventofcode.com/2017/day/7
#

def find_root(towers, is_sub):
    no_subs = []
    for t in towers.keys():
        if not t in is_sub:
            no_subs.append(t)
    assert len(no_subs) == 1, "More than one tower that is no sub-tower."
    return no_subs[0]

def parse(data_lines):
    '''Returns the root and towers structure.'''
    towers = {}
    is_sub = []
    for line in data_lines:
        line = line.replace('\n', '')
        sub_towers = []
        if ' -> ' in line:
            tower, sub_towers = line.split(' -> ')
        else:
            tower = line
        tower, weight = tower.split(' ')
        weight = int(weight.replace('(', '').replace(')', ''))
        if sub_towers:
            sub_towers = sub_towers.split(', ')
            is_sub += sub_towers
        towers[tower] = {'weight': weight, 'subs': sub_towers}
    return find_root(towers, is_sub), towers

def sum_sub_weights(towers, tower):
    def rec_sum(tower):
        return towers[tower]['weight'] +sum(map(rec_sum, towers[tower]['subs']))
    return rec_sum(tower)

def get_altered_element(d):
    keys = list(d.keys())
    for i in range(len(keys)):
        if d[keys[i]] != d[keys[i-1]] and d[keys[i]] != d[keys[i-2]]:
            return keys[i], d[keys[i]]
    return None, None

def find_wrong_weighted_tower(towers, tower):
    sub_weights = {}
    for sub in towers[tower]['subs']:
        sub_weights[sub] = sum_sub_weights(towers, sub)
    altered_tower, altered_weight = get_altered_element(sub_weights)
    if altered_tower is None:
        return tower
    else:
        return find_wrong_weighted_tower(towers, altered_tower)

def get_weight_correction(towers, wrong_weighted_tower):
    for parent_tower in towers:
        if wrong_weighted_tower in towers[parent_tower]['subs']:
            break
    for brother in towers[parent_tower]['subs']:
        if brother != wrong_weighted_tower:
            break
    wrong_weight = sum_sub_weights(towers, wrong_weighted_tower)                  
    others_weight = sum_sub_weights(towers, brother)
    return towers[wrong_weighted_tower]['weight'] - (wrong_weight - others_weight)

with open("day07.data", "r") as data:
    root, towers = parse(data.readlines())

print("Part 1: {}".format(root))
print("Part 2: {}".format(get_weight_correction(towers, find_wrong_weighted_tower(towers, root))))
