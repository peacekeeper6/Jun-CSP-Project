from week0.swapy import swap
from week0.keypady import matrix
import week0.tree
# import prefuncy
# import prefuncy2
# import week1.infodb


main_menu = [
    ["Swap", "week0/swapy.py"],
    ["Keypad", "week0/keypady.py"],
    ["Tree", "week0/tree.py"]
]

animationsub_menu = [
    ["Ship Animation", "week0/prefuncy.py"],
    ["Face Animation", "week0/prefuncy2.py"]
]

landlsub_menu = [
    ["InfoDB", "week1/infodb.py"],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)


def animationsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, animationsub_menu)

def landlsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, landlsub_menu)

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    menu_list.append(["Lists and Loops", landlsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
     menu()
