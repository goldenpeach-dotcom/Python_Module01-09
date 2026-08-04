import argparse

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs="*")
parsed = parser.parse_args()
#parsedにはプログラム名は含まれない
print(parsed.args)
