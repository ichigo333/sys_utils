import shutil

# path = "C:\\" # for windows
path = "/"

disk_stats = shutil.disk_usage(path)

total_space_bytes = disk_stats.total
used_space_bytes = disk_stats.used
free_space_bytes = disk_stats.free

print(f"total_space_bytes: {total_space_bytes}")
print(f"used_space_bytes: {used_space_bytes}")
print(f"free_space_bytes: {free_space_bytes}")

GB = 1024**3

total_space_gb = total_space_bytes / GB
used_space_gb = used_space_bytes / GB
free_space_gb = free_space_bytes / GB

print(f"total_space_gb: {total_space_gb: .2f} GB")
print(f"used_space_gb: {used_space_gb: .2f} GB")
print(f"free_space_gb: {free_space_gb: .2f} GB")

# print(2**30)
# print(GB)