""" print(f"First Module's Name: {__name__}")


def main():
    pass


# check if this file is being run directly or imported
if __name__ == "__main__":
    main() """

if __name__ == "__main__":
    print("Run Directly")
else:
    print("Run From Import")


