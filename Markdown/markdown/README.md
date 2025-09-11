
🌟 Ultimate Markdown Guide (Beginner → Advanced, A → Z)
🔹 1. Headings

Markdown headings # se banti hain.

# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
##### H5 Heading
###### H6 Heading


👉 Hidden Fact: Space dena (# Heading) recommended hai, lekin bina space bhi chalega (#Heading).

🔹 2. Paragraphs & Line Breaks

Normal likho to paragraph ban jata hai.
Line break ke liye 2 spaces + Enter lagao.

This is line one.  
This is line two.

🔹 3. Text Formatting
**Bold**
*Italic*
***Bold + Italic***
~~Strikethrough~~
<u>Underline (HTML)</u>


👉 Hidden Fact: __Bold__ aur _Italic_ bhi valid hai, alag style ke liye use hota hai.

🔹 4. Blockquotes
> Single quote
>> Nested quote

🔹 5. Lists
✅ Ordered List
1. First
2. Second
3. Third


👉 Agar tum sirf 1. hi likhte raho:

1. Apple
1. Banana
1. Mango


Output phir bhi proper numbering mai aayega.

✅ Unordered List
- Item
* Item
+ Item


👉 Teenon same kaam karte hain.

✅ Task Lists (Checklists)
- [x] Done
- [ ] Pending

🔹 6. Code
✅ Inline Code
`console.log("Hello Markdown")`

✅ Code Blocks
```js
console.log("Hello Markdown");
```


👉 Agar language mention na karo, tab bhi code show hoga but without syntax colors.

🔹 7. Links
✅ Simple Link
[Google](https://www.google.com)

✅ Tooltip (Advanced 🎯)
[Google](https://www.google.com "Search Engine")


👉 Tooltip tab dikhega jab mouse link par le jaoge.

🔹 8. Images
![Alt Text](https://via.placeholder.com/150)

✅ Image + Tooltip
![Logo](https://via.placeholder.com/150 "This is tooltip text")

✅ Image as Clickable Link
[![Logo](https://via.placeholder.com/150)](https://google.com)

🔹 9. Tables
| Name   | Age | City     |
|--------|-----|----------|
| Ali    | 25  | Karachi  |
| Ayesha | 22  | Lahore   |

✅ Alignment
| Left | Center | Right |
|:-----|:------:|------:|
| A    | B      | C     |

🔹 10. Horizontal Line
---


or

***

🔹 11. Emojis
:smile: :rocket: :fire:


👉 GitHub supported emoji shortcodes.

🔹 12. Footnotes
This is a sentence with a footnote.[^1]

[^1]: Footnote text goes here.

🔹 13. Collapsible Sections
<details>
<summary>Click to expand</summary>

Hidden content here...

</details>


👉 GitHub README mai content hide karne ke liye best.

🔹 14. Diagrams (Mermaid)
```mermaid
graph TD
A[Start] --> B{Decision}
B -->|Yes| C[Path 1]
B -->|No| D[Path 2]


👉 Flowcharts, sequence diagrams directly Markdown mai.  

---

## 🔹 15. Badges  

```md
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)


👉 GitHub projects mai status show karne ke liye.

🔹 16. Tooltips for Images (Meta Hack)
![Profile Pic](https://via.placeholder.com/100 "Hover text here")


👉 Ye GitHub pe mouse hover par extra info deta hai.

🔹 17. HTML Inside Markdown
<div align="center">
  <h3>Custom HTML inside Markdown</h3>
</div>


👉 HTML + Markdown mix kar sakte ho jab styling advance chahiye.

🔹 18. Best Practices

✅ Always use meaningful alt text for images
✅ Use headings hierarchically (H1 → H2 → H3)
✅ Keep line length under 80–100 chars for readability
✅ Add tooltips for better UX
✅ Use task lists for project tracking
✅ Collapse long sections with <details>

⚡ Hidden Pro Fact:
Markdown parser har platform pe thoda different behave karta hai (GitHub, Kaggle, Reddit, etc.) → Always test in your target platform.
