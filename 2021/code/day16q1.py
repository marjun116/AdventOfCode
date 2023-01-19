from io import StringIO
file = open("../inputs/day16.txt", "r")

hex = file.readline().strip()
binary = ''
for char in hex:
    currBinary = str(bin(int(char, 16))[2:].zfill(4))
    binary = binary + currBinary

totalVersion = 0


def read_packet(buffer):
    """Read a packet."""
    global totalVersion
    version = buffer.read(3)
    totalVersion += int(version, 2)
    type_id = buffer.read(3)

    if type_id == "100":
        chunks = []
        group = ""
        while group != "0":
            group = buffer.read(1)
            chunks.append(buffer.read(4))
        return int("".join(chunks), 2)

    packets = []
    if buffer.read(1) == "0":
        length = int(buffer.read(15), 2)
        target_length = buffer.tell() + length
        while buffer.tell() != target_length:
            packets.append(read_packet(buffer))
    else:
        num_packets = int(buffer.read(11), 2)
        for _ in range(num_packets):
            packets.append(read_packet(buffer))


read_packet(StringIO(binary))
print(totalVersion)
