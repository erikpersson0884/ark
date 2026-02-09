import json
from pathlib import Path

# =====================
# CONFIG
# =====================
BASE_DIR = Path(__file__).resolve().parent
RESOURCE_MAP_FILE = "resource_map.json"

INPUT_CONFIG_FILE = BASE_DIR / "item_costs.json"
OUTPUT_INI_FILE = BASE_DIR / "resourses.ini"


def load_resource_map(path):
    with open(path, "r") as f:
        raw_map = json.load(f)

    # Invert map: "Wood" -> "PrimalItemResource_Wood_C"
    return {v: k for k, v in raw_map.items()}


def generate_config(json_file, output_file, resource_map_file):
    resource_map = load_resource_map(resource_map_file)

    with open(json_file, "r") as f:
        data = json.load(f)

    lines = []

    for item_class, resources in data.items():
        resource_strs = []

        for res_name, amount in resources.items():
            ark_res = resource_map.get(res_name)
            if not ark_res:
                print(f"Warning: Resource '{res_name}' not in {RESOURCE_MAP_FILE} — skipped")
                continue

            resource_strs.append(
                f'(ResourceItemTypeString="{ark_res}",'
                f'BaseResourceRequirement={amount},'
                f'bCraftingRequireExactResourceType=false)'
            )

        if not resource_strs:
            continue

        resource_block = ", ".join(resource_strs)
        lines.append(
            f'ConfigOverrideItemCraftingCosts='
            f'(ItemClassString="{item_class}",'
            f'BaseCraftingResourceRequirements=({resource_block}))'
        )

    with open(output_file, "w") as f:
        f.write("\n".join(lines))

    print(f"Config written to {output_file}")


# =====================
# ENTRY POINT
# =====================
if __name__ == "__main__":
    generate_config(
        json_file=INPUT_CONFIG_FILE,
        output_file=OUTPUT_INI_FILE,
        resource_map_file=RESOURCE_MAP_FILE
    )
