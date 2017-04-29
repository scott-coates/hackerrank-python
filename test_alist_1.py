# json text file - make sure it's sorted alphabetically -children and roots too
import sys, json
from collections import defaultdict

# locations = json.load(sys.stdin)
locations = [
    {"id": 1, "name": "sf", "parent_id": None},
    {"id": 2, "name": "king st", "parent_id": 3},
    {"id": 3, "name": "soma", "parent_id": 1},
    {"id": 5, "name": "soma", "parent_id": None},
    {"id": 6, "name": "soma", "parent_id": 2},
]


# root = defaultdict(list)
#
# location_dict = {l['id']: (l['name'], l['parent_id']) for l in locations}
#
# for l in locations:
#     root[l['parent_id']].append(l['id'])
#
# ref = defaultdict(dict)
#
#
# def _get_parent(param):
#     l = location_dict[param]
#     if not l[1]:
#         if not ref[param]:
#             ref[param] = {'name': l[0], 'children': []}
#     else:
#         l = _get_parent(l[1])
#     return l
#
#
# for l in locations:
#     if not l['parent_id']:
#         ref[l['id']] = {'name': l['name'], 'children': []}
#     else:
#         parent = _get_parent(l['parent_id'])
#         parent['children'].append(ref[l['id']])
#
# print(locations)
#
#

def build_tree(nodes):
    # create empty tree to fill
    tree = {}

    # fill in tree starting with roots (those with no parent)
    build_tree_recursive(tree, None, nodes)

    return tree


def build_tree_recursive(tree, parent, nodes):
    # find children
    children = [n for n in nodes if n['parent_id'] == parent]

    # build a subtree for each child
    for child in children:
        # start new subtree
        tree[child['id']] = {}

        # call recursively to build a subtree for current node
        build_tree_recursive(tree[child['id']], child['id'], nodes)


print(build_tree(locations))
