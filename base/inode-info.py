#!/usr/bin/python3

import os
import stat
from datetime import datetime

file_path = "vars.py"  # Change this

# Get file stats
stat_info = os.stat(file_path)

# Convert timestamps to readable format
def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Permissions
permissions = stat.filemode(stat_info.st_mode)

# Print inode and block details
print(f"File: {file_path}")
print(f"Inode Number: {stat_info.st_ino}")
print(f"Device ID: {stat_info.st_dev}")
print(f"Number of Hard Links: {stat_info.st_nlink}")
print(f"Size: {stat_info.st_size} bytes")
print(f"Blocks Allocated: {stat_info.st_blocks}")  # Blocks allocated to the file
print(f"Block Size: {stat_info.st_blksize} bytes")  # Block size used for I/O
print(f"Last Access Time: {format_time(stat_info.st_atime)}")
print(f"Last Modification Time: {format_time(stat_info.st_mtime)}")
print(f"Last Metadata Change Time: {format_time(stat_info.st_ctime)}")
print(f"File Mode (Permissions): {permissions}")
print(f"Owner User ID: {stat_info.st_uid}")
print(f"Owner Group ID: {stat_info.st_gid}")

mline = """
📌 Why is 142 bytes using 8 blocks?
Filesystem Blocks Are Fixed Size

Most Linux filesystems (like ext4) allocate blocks in fixed sizes, often 4 KB (4096 bytes).
Even if a file is smaller than a block, it still takes up a full block.
If the file grows beyond a single block, more blocks are allocated.
Each Block is 512 Bytes in st_blocks

The st_blocks field counts 512-byte blocks (not 4 KB!).
st_blocks = 8 means 8 × 512 = 4096 bytes allocated, which equals one 4 KB block.
File Metadata and Fragmentation Overhead

Small files still consume full blocks due to how storage works.
If a file is heavily fragmented, it may use more blocks than necessary.
🔹 Example Calculation
Size of file: 142 bytes
Block size (st_blksize): 4096 bytes
Blocks allocated (st_blocks): 8 × 512 = 4096 bytes
Why 8 blocks? Because st_blocks reports in 512-byte units, and one 4 KB block = 8 × 512.
"""
