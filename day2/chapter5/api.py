states = {
    'South East' : ['Imo', 'Abia', 'Enugu', 'Anambra'],
    'South West' : ['Lagos', 'Ibadan', 'Ogun', 'Ondo'],
    'North West' : ['Kastina', 'Gombe', 'Jigawa', 'Kano'],
}

print(states['South West'][0])
for zones in states:
    print(zones.lower())
    for s in states[zones]:
        print(s.upper())