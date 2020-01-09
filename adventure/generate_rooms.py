from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import *
import uuid
import random


class Room_generator:


    def __init__(self):

        self.adjectives = ['burnt', 'wide', 'narow', 'green', 'red', 'yellow', 'tall',
                      'big', 'small', 'forked', 'dark']

        self.features = ['lake', 'forest', 'canyon', 'draw', 'creek', 'mesa', 'desert',
                    'plain', 'swamp', 'hill', 'mountain', 'river', 'valley', 'brush']

        self.storage = {}


    def generate(self, limit):
        initial_x = 0
        initial_y = 0

        for i in range(0, limit):

            # Generate a room title
            room_title = random.choice(self.adjectives) + ' ' + random.choice(self.features)

            # Create a room and add it to storage
            self.storage[room_title] = Room(title = room_title, id = i,
                position_x = initial_x, position_y = initial_y)

            # Save the new room
            self.storage[room_title].save()

            # If there is more than 1 room
            if len(self.storage.keys()) > 1:

                # List of tuples (class method, direction string)
                directions = [(self.storage[previous_room_title].n_to, 'n'),
                              (self.storage[previous_room_title].s_to, 's'),
                              (self.storage[previous_room_title].e_to, 'e'),
                              (self.storage[previous_room_title].w_to, 'w')]

                # Make a random choice
                direction = random.choice(directions)

                # While the direction is already populated pick another direction
                while direction[0] != 0:
                    direction = random.choice(directions)

                # Connect the rooms
                self.storage[previous_room_title].connectRooms(self.storage[room_title], direction[1])

                if direction[1] == 'n':
                    initial_y += 1
                elif direction[1] == 's':
                    initial_y -= 1
                elif direction[1] == 'e':
                    initial_x += 1
                elif direction[1] == 'w':
                    initial_x -= 1

            # Set the room as the previous room
            previous_room_title = room_title

            # Incriment or decriment position
            
            

