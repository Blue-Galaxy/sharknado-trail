import random

adjectives = ['burnt', 'wide', 'narrow', 'green', 'red', 'yellow', 'tall',
                'big', 'small', 'forked', 'dark']

features = ['lake', 'forest', 'canyon', 'draw', 'creek', 'mesa', 'desert',
            'plain', 'swamp', 'hill', 'mountain', 'river', 'valley', 'brush']


def make_name_desc():
    room_adj = random.choice(adjectives)
    room_feat = random.choice(features)
    name = f"{room_adj} {room_feat}"
    desc = F"You see a {room_adj} looking {room_feat}."
    return name, desc