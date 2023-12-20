import os

os.chdir("Photos")
originals = os.listdir()
places = []
# Print out the list, just to be sure you're getting the results you expect:
# print(originals)

def extract_place(filename):
    # first = filename.find("_") # Find the first underscore
    # partial = filename[first+1:] # Get the slice from location of first underscore to the end
    # second = partial.find("_")
    # return partial[:second]
    return filename.split("_")[1] #separate out the punctuations, [1] is to select the second item in list


def sort_place(originals):
    for filename in originals:
        extract_place(filename)
    return places.append(extract_place(filename))


print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place("2018-01_Scottland_11/51/27.jpg"))

print(sort_place(originals))
print(places)
print(originals)