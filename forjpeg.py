def jpeg_segs(data):
    i = 2  # skip FF D8 aka start of scan, sos
    while i < len(data):
        if data[i] != 0xFF: # sumting wrong
            print("Broken file", i)
            return
        type = data[i + 1]
        length = int.from_bytes(data[i + 2:i + 4], "big")
        print(f"{type:02X}  {length} bits")

        if type== 0xDA:
            return
        i = i + 2 + length
