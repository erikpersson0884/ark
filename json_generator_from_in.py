import json
import re
from colorama import init, Fore

init(autoreset=True)  # Add this after imports


# =====================
# CONFIG
# =====================
INPUT_CONFIG_FILE = "Game.ini"
OUTPUT_JSON_FILE = "resources.json"

RESOURCE_MAP_FILE = "resource_map.json"

# =====================
# REGEX
# =====================
ITEM_REGEX = re.compile(
    r'ItemClassString="([^"]+)"'
)

RESOURCE_REGEX = re.compile(
    r'ResourceItemTypeString="([^"]+)",BaseResourceRequirement=([\d.]+)'
)

# =====================
# HELPERS
# =====================
def load_resource_map(path):
    with open(path, "r") as f:
        return json.load(f)

# =====================
# MAIN LOGIC
# =====================
def parse_config(input_file, output_file, resource_map_file):
    resource_map = load_resource_map(resource_map_file)
    result = {}

    with open(input_file, "r") as f:
        for line in f:
            if "ConfigOverrideItemCraftingCosts" not in line:
                continue

            item_match = ITEM_REGEX.search(line)
            if not item_match:
                continue

            item_class = item_match.group(1)
            resources = {}

            for res_class, amount in RESOURCE_REGEX.findall(line):
                res_name = resource_map.get(res_class)
                if not res_name:
                    print(f"{Fore.RED}Warning: Unknown resource '{res_class}', skipping.")
                    continue

                resources[res_name] = int(float(amount))

            result[item_class] = resources

    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"JSON written to {output_file}")

# =====================
# ENTRYPOINT
# =====================
if __name__ == "__main__":
    parse_config(
        input_file=INPUT_CONFIG_FILE,
        output_file=OUTPUT_JSON_FILE,
        resource_map_file=RESOURCE_MAP_FILE
    )
