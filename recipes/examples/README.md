# Contribution spec

Every recipe lives in its own directory under `recipes/`, named after the
recipe itself.

A complete recipe contribution must contain both of the following files:

1. `docs/recipe.md` - the recipe document for the dish.
2. `evaluation/quality_check.py` - the quality-check script for the recipe.

Beyond the presence of these two required files, no other content details are
enforced: a recipe with both required files in place satisfies the spec, and a
recipe that is still missing either required file does not.

See `classic-margherita-pizza/` for a complete sample contribution.
