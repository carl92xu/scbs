# DECLARE roomWidth, roomHeight, roomLength, unpaintableArea, coat, paintRequired: INTEGER


# FUNCTION paint_required() RETURN paintRequired:INTEGER
def paint_required():
    # OUTPUT "Room Width: "
    # INPUT roomWidth
    roomWidth = input("Room Width: ")
    # OUTPUT "Room Height: "
    # INPUT roomHeight
    roomHeight = input("Room Height: ")
    # ...
    roomLength = input("Room Length: ")
    # ...
    unpaintableArea = input("Unpaintable Area: ")
    # ...
    coat = input("Number of Coat: ")
    # paintRequired <- ((roomHeight * roomLength * roomWidth) - unpaintableArea) * coat
    paintRequired = ((roomHeight * roomLength * roomWidth) - unpaintableArea) * coat
    # RETURN paintRequired
    return paintRequired


# OUTPUT paint_required()
print(paint_required())
