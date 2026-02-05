import os

def collect_primal_item_structures(root_dir):
    for _, _, files in os.walk(root_dir):
        for file in files:
            if file.startswith("PrimalItemStructure_"):
                yield file

def filter_wanted_files(filenames):
    keywords = ("stone", "wood", "metal")
    for name in filenames:
        if any(k in name.lower() for k in keywords):
            yield name

def replace_uasset(name):
    if name.lower().endswith(".uasset"):
        return name[:-7] + "_C"
    return name

if __name__ == "__main__":
    root_directory = "."
    output_file = "output.txt"

    files = collect_primal_item_structures(root_directory)
    filtered_files = filter_wanted_files(files)

    with open(output_file, "w", encoding="utf-8") as f:
        for name in filtered_files:
            final_name = replace_uasset(name)
            f.write(final_name + "\n")
            print(final_name)
