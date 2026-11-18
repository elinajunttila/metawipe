import sys


def recognize(data):
    if data[:2] == b"\xff\xd8":
        return "jpeg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return None


def main():
    if len(sys.argv) < 2:
        print("Use: python main.py photo.jpg")
        return

    polku = sys.argv[1]
    with open(path, "rb") as f:
        data = f.read()

    type = recognize(data)
    if type is None:
        print("Unknown file format")
    else:
        print("File format:", type)


if __name__ == "__main__":
    main()
