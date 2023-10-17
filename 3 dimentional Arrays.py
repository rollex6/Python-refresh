# Define the dimensions of the 3D array
num_buildings = 3
num_floors = 5
num_rooms = 10

# Create a 3-dimensional array to represent the rooms' occupancy
rooms = [[[True for _ in range(num_rooms)] for _ in range(num_floors)] for _ in range(num_buildings)]
print(rooms)
# Mark rooms as occupied
rooms[0] = [[True for _ in range(num_rooms)] for _ in range(num_floors)]  # All rooms occupied in the first building
rooms[1][1][2:10] = [False] * 8  # Only rooms 3 to 10 on the second floor of the second building are unoccupied
rooms[2] = [[False for _ in range(num_rooms)] for _ in range(num_floors)]  # All rooms are empty in the third building
rooms[2][0][0:10] = [True] * 10
print ('after filling rooms')
print (rooms)
# Calculate the total number of empty rooms
total_empty_rooms = sum(not room for building in rooms for floor in building for room in floor)

# Print the occupancy status of each room with True (occupied) and False (empty)
for building_idx, building in enumerate(rooms):
    for floor_idx, floor in enumerate(building):
        for room_idx, occupied in enumerate(floor):
            print(f"Building {building_idx+1}, Floor {floor_idx+1}, Room {room_idx+1}: {occupied}")

print(f"Total empty rooms: {total_empty_rooms}")