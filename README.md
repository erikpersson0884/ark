# ARK: Survival Evolved - Config Generator

[![Last Commit][last-commit-shield]][last-commit-url]
[![Repo Size][repo-size-shield]][repo-size-url]
[![Language][language-shield]][python-url]
[![License][license-shield]][license-url]
[![Author][author-shield]][author-url]



## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Files](#files)
5. [Step-by-Step Instructions](#step-by-step-instructions)
6. [Helpful Links](#helpful-links)
7. [License](#license)

---

## Overview
This project provides tools to generate and modify crafting cost overrides for **ARK: Survival Evolved**. It allows you to extract structures from the game, edit crafting costs in JSON format, and generate ready-to-use `overrides.ini` files for your `Game.ini`.


## Features
- Automatically detects all structures in ARK folders
- Generates correct Game.ini override syntax
- Supports bulk editing via JSON
- Reverse-engineers existing overrides


## Requirements
- python


## How to Use

1. Place `get_structure_names.py` in your mod folder or main ARK folder. Optionally, change the `rootdir` variable to the folder path you want to scan.  
2. Run `get_structure_names.py` → outputs `found_structures.txt` with all detected structures.  
3. Edit `item_costs.json` to define the items you want to change and their crafting components.  
4. Run `config_generator.py` → outputs `overrides.ini`.  
5. Copy `overrides.ini` into your `Game.ini` (read more about configuration files [here](https://ark.wiki.gg/wiki/Server_configuration#Configuration_Files)).

---

## Files

* **`get_structure_names.py`**  
  Scans all subfolders in its directory (or a specified folder) for structure files. Converts them to the correct `Game.ini` override syntax and saves them to `found_structures.txt`.  
  - Finds files named `PrimalItemStructure_<structure>.uasset`  
  - Converts them to `PrimalItemStructure_<structure>_C`

* **`resource_map.json`**  
  Maps actual resource IDs to human-readable names used in the application.

* **`config_generator.py`**  
  Reads `item_costs.json` and generates an `overrides.ini` file ready to paste into your `Game.ini`.

* **`json_generator_from_ini.py`**  
  Reverse-engineered tool that reads your `Game.ini` and extracts overrides into the `item_costs.json` format. Useful for bulk edits of your current configuration.

---



---

## Step-by-Step Instructions

1. **Scan for Structures**
   - Place `get_structure_names.py` in your mod folder or main ARK folder.  
   - Optionally, update the `rootdir` variable in the script to the folder path you want to scan.  
   - Run the script:  
     ```bash
     python get_structure_names.py
     ```
   - Output: `found_structures.txt` – a list of all detected structures in ARK override syntax.

2. **Edit Crafting Costs**
   - Open `item_costs.json` and add the items you want to modify.  
   - Example structure:
     ```json
     {
       "PrimalItemStructure_WoodGate_C": {
         "Wood": 20,
         "Thatch": 10
       },
       "PrimalItemStructure_MetalGate_C": {
         "MetalIngot": 15,
         "Wood": 5
       }
     }
     ```
   - The keys must match the structure names found in `found_structures.txt`. Values represent the amount of each resource required.

3. **Generate Overrides**
   - Run `config_generator.py`:
     ```bash
     python config_generator.py
     ```
   - Output: `overrides.ini` – ready to paste into your `Game.ini`.

4. **Apply to Game**
   - Copy the contents of `overrides.ini` into your `Game.ini` located in:
     ```
     ShooterGame/Saved/Config/WindowsServer/Game.ini
     ```
   - Restart your server or game for the changes to take effect.

5. **Optional: Reverse Engineer Existing Config**
   - Use `json_generator_from_ini.py` to extract your current overrides from `Game.ini` into `item_costs.json` format for bulk edits.

---

## Helpful Links

- [ARK IDs](https://arkids.net/) – Find IDs of structures and items  
- [ARK Wiki](https://ark.wiki.gg/) – Base resource costs and general game info  
- [Server Configuration](https://ark.wiki.gg/wiki/Server_configuration) – Complete list of server settings, including item crafting overrides  

---


## License
This project is licensed under the CC BY-NC-SA 4.0 License - see [LICENSE](LICENSE) for details.




---

<!-- Repo info Shields -->
[last-commit-shield]: https://img.shields.io/github/last-commit/erikpersson0884/ark.svg?style=for-the-badge
[last-commit-url]: https://github.com/erikpersson0884/ark/commits/main
[repo-size-shield]: https://img.shields.io/github/repo-size/erikpersson0884/ark?style=for-the-badge
[repo-size-url]: https://github.com/erikpersson0884/ark
[author-shield]: https://img.shields.io/badge/Author-Erik%20Persson-blue?style=for-the-badge
[author-url]: https://github.com/erikpersson0884
[license-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge
[license-url]: https://creativecommons.org/licenses/by-nc-sa/4.0/


<!-- Frameworks & Languages Shields -->
[language-shield]: https://img.shields.io/badge/Language-Python-306998?style=for-the-badge
[python-url]: https://www.python.org/
[LICENCE]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en