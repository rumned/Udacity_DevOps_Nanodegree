# Here is the example you can test it on:
lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

# Write your function definition here:
def breakify(target):
    return "<br>".join(target)
    
    
# Then call the function and print the results
print(breakify(lines))