scale = list(map(int, input().split()))
ascending_scale = sorted(scale)
descending_scale = sorted(scale, reverse=True)

if scale == ascending_scale:
    print("ascending")
elif scale == descending_scale:
    print("descending")
else:
    print("mixed")