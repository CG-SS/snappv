#!/usr/bin/env python3
"""
Generate a CRC32C lookup table using the reflected polynomial 0x82F63B78
(reflected form of 0x1EDC6F41) and output it as Vlang source code.
"""

POLY = 0x82F63B78  # Reflected form of the CRC32C polynomial 0x1EDC6F41


def generate_crc32c_table() -> list[int]:
    table = []
    for byte in range(256):
        crc = byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ POLY
            else:
                crc >>= 1
        table.append(crc & 0xFFFFFFFF)
    return table


def format_vlang_table(table: list[int]) -> str:
    # Format each entry as a hex literal with Vlang's u32() cast
    entries = [f"u32(0x{v:08x})" for v in table]

    # Lay out 4 entries per line for readability
    cols = 4
    rows = [entries[i : i + cols] for i in range(0, len(entries), cols)]
    inner = ",\n\t".join(", ".join(row) for row in rows)

    return f"const crc32c_table = [\n\t{inner},\n]!"


if __name__ == "__main__":
    table = generate_crc32c_table()
    print(format_vlang_table(table))
