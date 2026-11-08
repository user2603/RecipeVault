# RecipeVault

RecipeVault is the community cookbook we keep as a git repository. Every chef
on the team works on a personal branch, named after themselves, and pushes the
recipes they have been preparing there.

## Layout

- `recipes/examples/` - the contribution spec, including a complete sample recipe.
- `recipes/<recipe-name>/` - one directory per recipe.

## Reviewing recipes

New recipes are reviewed straight from each chef's branch. A reviewed recipe
gets an entry in the team's Notion registry, and every recipe that reaches
`published` status there is collected into the `menu` branch under
`recipes/menu/`.

> A recipe counts as `published` only when it satisfies the contribution spec
> in `recipes/examples/`; while anything required is still missing it stays
> `drafting`.

## Branch etiquette

Branches are personal - keep your recipes on your own branch until they have been reviewed.
