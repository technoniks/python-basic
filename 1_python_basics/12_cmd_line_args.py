import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("num1", help="First Number")
  parser.add_argument("num2", help="First Number")
  parser.add_argument("op", help="Operation")

  args = parser.parse_args()

  if args.op == "add":
    print(int(args.num1) + int(args.num2))
