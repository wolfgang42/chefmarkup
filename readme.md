ChefMarkup is a simple markup language (in the style of Markdown)
for creating two-column recipes with the instructions on the left and
the ingredients on the right, like this:

### Microwave Cheese Sauce
<table>
<tr valign="top"><td rowspan="1">In a large microwave safe glass bowl, heat until melted (about 50 seconds):</td>
<td>2 tablespoons butter</td>
</tr>
<tr valign="top"><td rowspan="2">Whisk the melted butter together with:</td>
<td>2 tablespoons flour</td>
</tr><tr>
<td>1 cup warm milk</td>
</tr>
<tr valign="top"><td rowspan="1">Add:</td>
<td>1 cup shredded cheddar cheese</td>
</tr>
<tr valign="top"><td rowspan="1">Place bowl in microwave and cook on high for 1½-2 minutes, whisking every 30 seconds or so, until sauce is thick and heated through.</td>
</tr>
<tr valign="top"><td rowspan="1">(optional)If desired, season with:</td>
<td>1/2 teaspoon salt</td>
</tr>
<tr valign="top"><td rowspan="1">Whisk until blended.</td>
</tr>
</table>
See markup: [Microwave Cheese Sauce.chefml](examples/Microwave Cheese Sauce.chefml)

I consider this format to be better than the traditional
ingredients-then-instructions format, because it puts all of the information
needed while cooking in one place, so I don't have to search through the list of
ingredients to determine a quantity while cooking.

## ChefMarkup Principles
ChefMarkup is based on the principle that the markup should be unobtrusive as
possible. It should also be possible to parse recipes by computer and create
features such as an ingredient index or a shopping list, though this has not
been implemented yet.
The cheese sauce recipe above provides an overview of the language;
check out [Stuffed Cabbage Rolls](examples/Stuffed Cabbage Rolls.chefml)
for more advanced features such as multiple sections, or look at the
[ChefML specification](./chefml-specification.md).
I will be adding more features as the need arises.

## Use
`recipe2html` is a simple python script which will generate an HTML file
from the `.chefml` file. Use it like this:
```bash
./recipe2html "examples/Microwave Cheese Sauce.chefml" > "examples/Microwave Cheese Sauce.html"
```

`parserecipe.py` does the heavy-duty parsing of the `.chefml` file and is
intended to be usable with several different converters other than the HTML
one. I haven't written any others yet, though. If you want to, the
output format is simple; it's just a lot of nested objects and arrays.
