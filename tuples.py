"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]



def convert_coordinate(coordinate):
    num, letter= coordinate[0], coordinate[1]
    return (int(num), letter)


def create_record(azara_record, rui_record):
    treasure, azara_coordinate = azara_record
    location, rui_coordinate, quadrant = rui_record
    
    rui_coordinate_str = rui_coordinate[0]+ rui_coordinate[1]
    if azara_coordinate == rui_coordinate_str:
        return (treasure, azara_coordinate, location, rui_coordinate, quadrant)
    else:
        return "no coincide"
