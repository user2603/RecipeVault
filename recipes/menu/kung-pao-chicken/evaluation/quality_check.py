#!/usr/bin/env python3
"""Quality check for the kung-pao-chicken recipe."""

REQUIRED_SECTIONS = ("Ingredients", "Instructions")

def check_recipe_document(path="docs/recipe.md"):
    with open(path, "r", encoding="utf-8") as fh:
        document = fh.read()
    missing = [s for s in REQUIRED_SECTIONS if "## " + s not in document]
    if missing:
        raise ValueError("recipe document is missing sections: " + ", ".join(missing))
    return True

if __name__ == "__main__":
    assert check_recipe_document()
    print("kung-pao-chicken: quality check passed")
