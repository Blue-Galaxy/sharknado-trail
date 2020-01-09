from adventure.models import Room, Player
from .name_generator import make_name_desc
from collections import deque
import uuid
import random


class Room_generator:

    def __init__(self, width: int, height: int, num_rooms: int):
        self.width = width
        self.height = height
        self.num_rooms = num_rooms
        self.grid = None
        self.room_count = 1


    def generate(self):
        self.grid = [None] * self.height
        for i in range(len(self.grid)):
            self.grid[i] = [None] * self.width

        # Start in the middle of the grid.
        mid_y = (self.height // 2)
        mid_x = (self.width // 2) - 1

        # Make the first room to add to our world. Place it in the center of the grid.
        name, desc = make_name_desc()
        first = Room(title=name,
                     description=desc,
                     position_x=mid_x,
                     position_y=mid_y)
        first.save()
        self.grid[first.position_y][first.position_x] = first.id

        # Place room number one in a queue.
        queue = deque()
        queue.append(first)

        # Keep making rooms until we've reached our desired number.
        while self.room_count < self.num_rooms:
            current_room = queue.popleft()

            # Connect another room to the current one in each available direction.
            for direction, delta_x, delta_y in zip(['n', 'w', 's', 'e'], [0, 1, 0, -1], [-1, 0, 1, 0]):
            # for direction, delta_x, delta_y in zip(['n', 'w', 'e', 's'], [0, 1, -1, 0], [-1, 0, 0, 1]):

                # If there's already a room this direction, keep going.
                if not eval(f'current_room.{direction}_to'):

                    # Check that we're still on the grid.
                    new_y = current_room.position_y + delta_y
                    if not self.height > new_y >= 0:
                        continue

                    new_x = current_room.position_x + delta_x
                    if not self.width > new_x >= 0:
                        continue

                    # Check that this grid space is open.
                    if not self.grid[new_y][new_x]:
                        # Make a new room, save it, connect it to the current room,
                        # and add it into the queue so we can add more rooms to it.
                        name, desc = make_name_desc()
                        next_room = Room(title=name,
                                         description=desc,
                                         position_x=new_x,
                                         position_y=new_y)
                        next_room.save()
                        self.grid[new_y][new_x] = next_room.id
                        current_room.connect_rooms(next_room, direction)
                        queue.append(next_room)
                        self.room_count += 1
                    else:
                        current_room.connect_rooms(Room.objects.get(id=self.grid[new_y][new_x]), direction)
        for row in self.grid:
            row.reverse()

        def print_rooms(self):
            """
            Print the rooms in self.grid in ascii characters.
            """
            # Add top border
            string = "# " * ((3 + self.width * 5) // 2) + "\n"

            for row in self.grid:
                # PRINT NORTH CONNECTION ROW
                row = list(reversed(row))
                string += "#"
                for room in row:
                    if room and Room.objects.filter(id=room)[0].n_to != 0:
                        string += "  |  "
                    else:
                        string += "     "
                string += "#\n"
                # PRINT ROOM ROW
                string += "#"
                for room in row:
                    if room and Room.objects.filter(id=room)[0].w_to != 0:
                        string += "-"
                    else:
                        string += " "
                    if room is not None:
                        string += f"{Room.objects.filter(id=room)[0].id}".zfill(3)
                    else:
                        string += "   "
                    if room and Room.objects.filter(id=room)[0].e_to != 0:
                        string += "-"
                    else:
                        string += " "
                string += "#\n"
                # PRINT SOUTH CONNECTION ROW
                string += "#"
                for room in row:
                    if room and Room.objects.filter(id=room)[0].s_to != 0:
                        string += "  |  "
                    else:
                        string += "     "
                string += "#\n"

            # Add bottom border
            string += "# " * ((3 + self.width * 5) // 2) + "\n"

            # Print string
            print(string)

def main():
    """Run script to populate database with rooms and items."""
    # Room.objects.all().delete()
    # num_rooms = 100
    # width = 15
    # height = 15

    # w = Room_generator(width, height, num_rooms)
    # w.generate()
    w.print_rooms()

    print('World Created!! Good Job!')
    print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {w.room_count}\n")


if __name__ == "__main__":
    main()


