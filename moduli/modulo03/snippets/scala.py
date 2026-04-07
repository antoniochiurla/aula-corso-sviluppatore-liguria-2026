coords = [487,661,  501,579,
          570,546,  613,348,
          759,268,  826,270,
          834,286,  951,367,
          996,544,  1083,607,
          1081,669]

new_coords = []

for coord in coords:
    new_coords.append(str(coord * 520 // 1536))
print(",".join(new_coords))