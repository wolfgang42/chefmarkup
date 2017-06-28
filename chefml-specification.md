# ChefML Specification
_**Note**: this document is a draft.
The example recipes, as well as `parserecipe.py` itself,
should be consulted if you have any questions._

ChefMarkup files have two parts: metadata and recipe.
These are separated from each other by four dashes ('`----`') on a separate line.

## Metadata
The metadata is in [YAML](http://www.yaml.org) format.
Other than the requirement that there be a `title` key,
the current version of the specification does not cover the format of this part.

## Recipe
* The recipe is composed of one or more _instructions_.
* An **instruction** is a line of text (to be placed in the left column of the recipe),
  followed by zero or more _ingredients_.
  The string '`(optional)`' at the beginning of an instruction indicates that this instruction--and all of its ingredients--are optional.
* An **ingredient** is the part which is placed in the right column;
  it is associated with the preceding instruction.
  An ingredient is indicated with a tab at the beginning of the line.
  (Spaces currently cannot be substituted.)
  The string '`(optional)`' at the beginning of an ingredient indicates that this ingredient--and all of its _alternatives_--are optional.
* An ingredient may have **alternatives**.
  These are listed on the lines following the first line of the ingredient,
  and each line begins with a tab, at least two spaces, and the string '`OR `'.
