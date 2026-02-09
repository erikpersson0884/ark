import os

keywords = ("stone", "wood", "metal")
output_file = "found_structures.txt"
root_directory = "."


def collect_all_structures_files(root_dir):
    for _, _, files in os.walk(root_dir):
        for file in files:
            if file.startswith("PrimalItemStructure_"):
                yield file


def filter_wanted_files(filenames):
    for name in filenames:
        if any(k in name.lower() for k in keywords):
            yield name


def replace_uasset(name):
    if name.lower().endswith(".uasset"):
        return name[:-7] + "_C"
    return name


def rewrite_filesnames_to_structures(filenames):
    return [replace_uasset(name) for name in filenames]

def save_to_file(structures, filename=output_file):
    with open(filename, "w", encoding="utf-8") as f:
        for structure in structures:
            f.write(structure + "\n")

def print_results(structures):
    number_of_structures = len(structures)
    if number_of_structures == 0:
        print("No structures found.")
    else:
        print(f"Found {number_of_structures} structures:")
        for structure in structures:
            print(f" - {structure}")

def main():
    files = collect_all_structures_files(root_directory)
    filtered_files = filter_wanted_files(files)
    structures = rewrite_filesnames_to_structures(filtered_files)
    save_to_file(structures)
    print_results(structures)


if __name__ == "__main__":
    main()
