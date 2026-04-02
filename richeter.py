magnitude = float(input("Enter the earthquake magnitude on the Richter scale: "))

if magnitude >= 0:
    if magnitude < 2.0:
        category = "Micro earthquake (usually not felt)"
    else:
        if magnitude < 4.0:
            category = "Minor earthquake (felt, but rarely causes damage)"
        else:
            if magnitude < 5.0:
                category = "Light earthquake (minor damage possible)"
            else:
                if magnitude < 6.0:
                    category = "Moderate earthquake (may cause slight damage)"
                else:
                    if magnitude < 7.0:
                        category = "Strong earthquake (can be destructive)"
                    else:
                        if magnitude < 8.0:
                            category = "Major earthquake (serious damage)"
                        else:
                            category = "Great earthquake (can cause serious destruction)"
else:
    category = "Invalid magnitude"

print(f"Magnitude {magnitude} is classified as: {category}")