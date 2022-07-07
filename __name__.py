# __name__ is a Special Variable
# when we export this file everything in this file will be executed each time any file having import __name__ command
# we don't want this because it's the welcome page & it should not welcome again and again when running other programs,
# so we use __name__ i.e. the contents of main file will only print when this file is executing
def main():
    print("Hello")
    print("Welcome User")


if __name__ == "__main__":
    main()
