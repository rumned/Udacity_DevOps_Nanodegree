import os

def extract_place(filename):
    return filename.split('_')[1]


def make_places_directory(places):
        for place in places:
            os.mkdir(place)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_places_directory(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


# organize_photos("Photos")
print("TEST!")