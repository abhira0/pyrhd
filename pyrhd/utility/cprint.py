from sty import RgbFg, Style, bg, ef, fg, rs

"""To know more about sty module
https://github.com/feluxe/sty
"""
# Eg to create a new color
fg.orange = Style(RgbFg(255, 150, 50))


def aprint(*args, sup_err: bool = False, sep: str = " ", end: str = "\n", **kwargs):
    """Alternative Print\n
    Eg:\n
        ("a--", (10, 15, 20), "b--", "red", "g--", "green", sep="\\n")\n
        ("Prints in green","green")

    Args:
        sup_err (bool, optional): Suppress errors/exceptions showing on terminal. Defaults to False.
        sep (str, optional): seperator used if the elements are more than 1 to print. Defaults to " ".
    """
    for i in range(0, len(args), 2):
        clr = args[i + 1]
        if type(clr) == int:
            para = fg(clr)
        elif type(clr) == str:
            try:
                para = fg.__getattribute__(clr)
            except Exception as e:
                if sup_err:
                    continue
                print("-" * 20)
                print(e)
                print("\tTry to create custom color using sty module as shown below")
                print("\tfg.orange = Style(RgbFg(255, 150, 50))")
                print("-" * 20)
                continue
        elif len(clr) == 3:
            para = fg(*clr)
        else:
            continue
        print(para + str(args[i]) + fg.rs, end=sep)
    print(end=end)
