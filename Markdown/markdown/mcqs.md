

## 📝 Questions

---

### 1. You want to create a clickable image that leads to `https://example.com` and shows a tooltip "Homepage" when hovered. Which syntax is correct and will render the tooltip correctly?

```markdown
a) [![Alt Text](image.png "Homepage")](https://example.com)
b) [[Alt Text](image.png)](https://example.com "Homepage")
c) [![Alt Text](image.png)](https://example.com "Homepage")
d) [![Alt Text](image.png)](https://example.com)( "Homepage")
e) Both a and c are correct.
```

---

### 2. Analyzing the structure of a clickable image `[![Text](img.jpg)](link.com)`, what is the purpose of the exclamation mark `!` inside the square brackets?

```markdown
a) It makes the entire image element clickable.
b) It denotes that the link is an image source rather than a regular URL.
c) It is the standard syntax for defining an image element before it is wrapped with a link.
d) It is invalid syntax and should be omitted for clickable images.
e) It prioritizes the image loading for better performance.
```

---

### 3. You are creating a complex nested list with a numbered sub-list under a bulleted item. Which syntax will render without errors and with correct indentation?

```markdown
a) - Item One
     1. Sub-item One
     2. Sub-item Two
   - Item Two

b) * Item One
       1. Sub-item One
       2. Sub-item Two
   * Item Two

c) + Item One
       1. Sub-item One
       2. Sub-item Two
   + Item Two

d) All of the above are correct and will render identically.
e) Only a and b are correct, as the `+` symbol cannot be used for mixed list types.
```

---

### 4. You need to create a list where the numbering continues sequentially after an interrupting paragraph. How do you achieve this?

```markdown
a) Use HTML `<ol>` tags for precise control over numbering.
b) Use the same indentation level for the paragraph as the list items.
c) This is impossible in standard Markdown; the list will always restart.
d) Use a backslash `\` after the list item to continue the sequence.
e) Use the `start="X"` attribute on the subsequent list.
```

---

### 5. For a tooltip on a standard, non-clickable image, where exactly must the tooltip text be placed in the syntax `![Alt text](image.jpg)`?

```markdown
a) ![Alt text "tooltip"](image.jpg)
b) ![Alt text](image.jpg, "tooltip")
c) ![Alt text](image.jpg "tooltip")
d) ![Alt text](image.jpg)[^1] and [^1]: tooltip
e) Tooltips are only supported for clickable images, not standard ones.
```

---

### 6. You want a bulleted list using the `-` symbol to have a sub-list using the `*` symbol. What is the critical formatting rule for the sub-list to render correctly?

```markdown
a) The sub-list must be indented by exactly four spaces or one tab relative to the parent bullet.
b) The sub-list must use a different bullet character than its parent list.
c) The sub-list must be prefixed with a `+` symbol to indicate a new level.
d) The sub-list items must be on the same line as the parent item, separated by a semicolon.
e) There is no rule; any indentation will work as long as it's more than the parent.
```

---

### 7. Consider this code for a clickable image with a tooltip. What is the final destination of the link, and what tooltip text will be shown?  
`[![Logo](logo.png "The Logo")](https://site.com "The Site")`

```markdown
a) Link: logo.png, Tooltip: "The Logo"
b) Link: https://site.com, Tooltip: "The Site"
c) Link: https://site.com, Tooltip: "The Logo"
d) Link: https://site.com, Tooltip: "The Logo - The Site"
e) The syntax is invalid and will not render any link or image.
```

---

### 8. In a numbered list, if you write `1.` for every item instead of incrementing the number, how will most Markdown parsers render it?

```markdown
a) It will cause a syntax error and break the list.
b) It will render a list starting at 1 but showing the same number for every item.
c) It will automatically correct the numbering and display a sequentially ordered list (1, 2, 3...).
d) It will render a bulleted list instead of a numbered one.
e) It will ignore the numbers and show no list at all.
```

---

### 9. Which of the following statements about tooltips in Markdown is **UNEQUIVOCALLY FALSE**?

```markdown
a) Tooltip text can contain other Markdown formatting like **bold**.
b) The tooltip title attribute is part of the underlying HTML `<a>` or `<img>` tag.
c) Tooltips for links and images use the same syntax for the title attribute.
d) Single quotes (' '), double quotes (" "), and parentheses (( )) are all interchangeable for enclosing tooltip text.
e) A tooltip can be applied to a standard image even if it's not inside a link.
```

---

### 10. You have a long, complex nested list mixing ordered, unordered, and task lists. What is a common "best practice" to ensure it renders correctly across different platforms?

```markdown
a) Avoid mixing list types within the same nested structure.
b) Use only tabs for indentation, never spaces.
c) Preview the output in the target platform's renderer (e.g., GitHub).
d) Use HTML lists (`<ul>`, `<ol>`, `<li>`) for absolute control.
e) Both c and d are valid best practices for complex scenarios.
```



## 📚 Detailed Explanations

---

### 1. ✅ Correct Answer: **c**

```markdown
[![Alt Text](image.png)](https://example.com "Homepage")
```

- The tooltip (`"Homepage"`) belongs to the **outer link**, not the inner image.
- Option **a** places the tooltip on the image — which is overridden by the link’s tooltip.
- Option **b** is invalid syntax — no `!` for image.
- Option **d** has malformed syntax — parentheses outside the link.

> 💡 **Pro Tip**: In `[![img](src "img_title")](url "link_title")`, only `"link_title"` is visible as tooltip.

---

### 2. ✅ Correct Answer: **c**

> `!` is the standard syntax for defining an image element before it is wrapped with a link.

- `![ ]` = image
- `[ ]` = link
- So `[![ ]]()` = link wrapping an image

---

### 3. ✅ Correct Answer: **d**

> All of the above are correct and will render identically.

- `-`, `*`, `+` are **interchangeable** for unordered lists in Markdown.
- As long as indentation is correct (usually 2–4 spaces), all render the same.

---

### 4. ✅ Correct Answer: **a**

> Use HTML `<ol>` tags for precise control over numbering.

- Standard Markdown **cannot** resume numbering after a paragraph.
- Example:
  ```html
  <ol>
    <li>Item 1</li>
  </ol>
  <p>Some text</p>
  <ol start="2">
    <li>Item 2</li>
  </ol>
  ```

---

### 5. ✅ Correct Answer: **c**

```markdown
![Alt text](image.jpg "tooltip")
```

- Tooltip syntax is **same for images and links**: space + quoted string after URL.
- Works for **both** standalone and clickable images.

---

### 6. ✅ Correct Answer: **a**

> The sub-list must be indented by exactly four spaces or one tab relative to the parent bullet.

- Bullet character (`-`, `*`, `+`) doesn’t matter.
- **Indentation level** defines nesting — not the symbol.

---

### 7. ✅ Correct Answer: **b**

> **Link**: `https://site.com`, **Tooltip**: "The Site"

- For clickable images, **link’s tooltip overrides image’s tooltip**.
- Image’s `"The Logo"` is **ignored** in favor of link’s `"The Site"`.

---

### 8. ✅ Correct Answer: **c**

> It will automatically correct the numbering and display a sequentially ordered list (1, 2, 3...).

- Markdown parsers **auto-correct** numbered lists — you can write `1.` for all items.
- Output will be `<ol><li>...</li><li>...</li></ol>` → rendered as 1, 2, 3...

---

### 9. ✅ Correct Answer: **d**

> ❌ FALSE: Single quotes, double quotes, and parentheses are all interchangeable for enclosing tooltip text.

- ✅ `"(title)"` and `'(title)'` → valid
- ❌ `(title)` → **invalid** — parentheses alone are NOT valid for tooltips.

---

### 10. ✅ Correct Answer: **e**

> Both c and d are valid best practices for complex scenarios.

- **c**: Always preview in target renderer (GitHub, VS Code, etc.) — parsers vary.
- **d**: For mission-critical formatting, **HTML gives 100% control**.

---


