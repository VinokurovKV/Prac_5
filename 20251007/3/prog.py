lines = []
while (s := input()):
    lines.append(s)

height = len(lines)
width = len(lines[0])

gas_count = 0
liquid_count = 0

for i in range(1, height - 1):
    for j in range(1, width - 1):
        if lines[i][j] == '.':
            gas_count += 1
        elif lines[i][j] == '~':
            liquid_count += 1

total_volume = gas_count + liquid_count

rotated = []
rotated.append('#' * height)

for j in range(width - 2, 0, -1):
    row = ['#']
    for i in range(1, height - 1):
        row.append(lines[i][j])
    row.append('#')
    rotated.append(''.join(row))

rotated.append('#' * height)

rotated_height = len(rotated)
rotated_width = len(rotated[0])

available_liquid_height = liquid_count // (rotated_width - 2)

final_rotated = []
final_rotated.append(rotated[0])

for i in range(1, rotated_height - 1):
    if i <= rotated_height - 2 - available_liquid_height:
        row = '#' + '.' * (rotated_width - 2) + '#'
    else:
        row = '#' + '~' * (rotated_width - 2) + '#'
    final_rotated.append(row)

final_rotated.append(rotated[-1])

for row in final_rotated:
    print(row)

print()

gas_width = round(20 * gas_count / total_volume)
liquid_width = round(20 * liquid_count / total_volume)

while gas_width + liquid_width > 20:
    if gas_width > liquid_width:
        gas_width -= 1
    else:
        liquid_width -= 1

while gas_width + liquid_width < 20:
    if gas_width > liquid_width:
        liquid_width += 1
    else:
        gas_width += 1

gas_bar = '.' * gas_width
liquid_bar = '~' * liquid_width

gas_fraction = f"{gas_count}/{total_volume}"
liquid_fraction = f"{liquid_count}/{total_volume}"

max_fraction_length = max(len(gas_fraction), len(liquid_fraction))

print(f"{gas_bar} {gas_fraction:>{max_fraction_length}}")
print(f"{liquid_bar} {liquid_fraction:>{max_fraction_length}}")