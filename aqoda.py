class Command:
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def get_commands_from_file_name(self):
        commands = []
        file = open(filename, "r")
        while(True):
            line = file.readline().rstrip().strip()
            if (line != ""):
                words = line.split(" ")
                command = Command(words[0], words[1:]) 
                commands.append(command)
            else:
                break

        return commands

    def __str__(self):
        return "{} {}".format(self.name, self.params)

class Hotel:

    # TODO: แก้ชื่อ floor, room, numberOfFloor, numberOfRoom ให้เป็นพหูพจน์

    def __init__(self):
        self.floor = []
        self.room = []

    def generate_floor_room(self, numberOfFloor, numberOfRoom):
        for i in range(numberOfFloor):
            self.floor.append(i + 1)
            for j in range(numberOfRoom):
                room_number = str(i + 1) + str(j + 1).zfill(2)      
                self.room.append(room_number)

        return self.floor, self.room

    # def generate_keycard(self, numberOfKeycard):
    #     Room.keycards[room] = keycard

    #     return 

# TODO: สร้าง keycards ตอน check-in

class Room:
    keycards = {}

class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# TODO: BookList จาก list เป็น dict

class BookList:
    book_list = []

    def __init__(self, name, age, room, keycard):
        self.name = name
        self.age = age
        self.room = room
        self.keycard = keycard

class Reception:
    def book(self, age, room, keycard):
        if len(BookList.book_list) == 0:
            guest = BookList(name, age, room, keycard)
            BookList.book_list.append(guest)

        for i in BookList.book_list:
            if room in i.room:
                return i.name
            else:
                guest = BookList(name, age, room, keycard)
                BookList.book_list.append(guest)
                return name
                
if __name__ == "__main__":
    filename = "input.txt"
    commands = Command.get_commands_from_file_name(filename)
    hotel = Hotel()
    keycard = 0

    for command in commands:
        if command.name == "create_hotel":
            numberOfFloor = command.params[0]
            numberOfRoom = command.params[1]
            generate_floor_room = hotel.generate_floor_room(int(numberOfFloor), int(numberOfRoom))
            print("Hotel created with " + numberOfFloor + " floor(s), " + numberOfRoom + " room(s) per floor.")

        # TODO: ทำ check-in

        if command.name == "book":
            keycard = keycard + 1
            room = command.params[0]
            name = command.params[1]
            age = command.params[2]
            guest = Guest(name, age)
            name_book = Reception.book(guest.name, guest.age, room, Room.keycards.get(room))
            if name_book != name:
                print("Cannot book room " + room + " for " + name + ", The room is currently booked by " + name_book + ".")
            else:
                print("Room " + room + " is booked by " + name + " with keycard number " + str(Room.keycards.get(room)) + ".")

            # print(floor,name,age)
