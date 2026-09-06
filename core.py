def generate_new_name(name, prefix="", suffix="", find="", replace="", number=None):
    if find:
        name = name.replace(find, replace)

    if prefix:
        name = prefix + name

    if number is not None:
        name = name + "_" + str(number).zfill(2)
        
    if suffix:
        name = name + suffix

    return name

if __name__ == "__main__":
    print(generate_new_name("Rock", prefix="SM_", suffix=".fbx"))
    print(generate_new_name("Rock", find="Rock", replace="Boulder"))
    print(generate_new_name("Rock", prefix="SM_", number=3))