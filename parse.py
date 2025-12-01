import argparse

def listening():
    parser = argparse.ArgumentParser()

    parser.add_argument("command", help="starts add sequence")
    parser.add_argument("--description", help="sets expense description")
    parser.add_argument("--amount", help="sets expense amount", type=int)
    return parser.parse_args()