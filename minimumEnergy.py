def calculate_energy(n, x1, y1, x2, y2):
    layer_start = min(abs(x1 - (n // 2)), abs(y1 - (n // 2)))
    layer_target = min(abs(x2 - (n // 2)), abs(y2 - (n // 2)))

    movements_to_outer_start = abs(layer_start - layer_target)
    movements_to_outer_target = abs(layer_start - layer_target)

    movements_horizontal = abs(x1 - x2)
    movements_vertical = abs(y1 - y2)

    total_movements = (
        movements_to_outer_start +
        movements_to_outer_target +
        movements_horizontal +
        movements_vertical
    )

    print(total_movements)


calculate_energy(4, 1, 4, 3, 3)
