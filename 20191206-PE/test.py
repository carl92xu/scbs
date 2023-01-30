for i in range(1, 101):
    delay_index = (100 - i)/500
    if delay_index < 0.15:
        delay_index = 0.1
    print(delay_index)
