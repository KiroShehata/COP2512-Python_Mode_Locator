def print_mode():
    while True:
        user_input = input("Enter some integers: ")
        
        if not user_input.strip():
            print("ERROR - give me some values!")
            continue
        
        try:
            numbers = list(map(int, user_input.split()))
        except ValueError:
            print("ERROR - all values must be integers!")
            continue
        out_of_range = [num for num in numbers if num < 0 or num > 10]
        if out_of_range:
            for num in out_of_range:
                print(f"ERROR - value {num} is out of range!")
            continue
        
        
        break
    
    count= {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
        
    mode = max(count, key=lambda k: count[k])
    print(f"Mode = {mode}")