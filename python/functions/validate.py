def validate(parameter:float, restraint:float, mode:str, para_name:str):
    if mode == "<":
        if not parameter < restraint:
            print(f"{para_name} = {parameter} < {restraint} not satisfied!")
            exit(-1)
    elif mode == "=":
        if not parameter == restraint:
            print(f"{para_name} = {parameter} = {restraint} not satisfied!")
            exit(-1)
    elif mode == ">":
        if not parameter > restraint:
            print(f"{para_name} = {parameter} > {restraint} not satisfied!")
            exit(-1)
    else:
        print("Invalid validate mode!")
        exit(-1)