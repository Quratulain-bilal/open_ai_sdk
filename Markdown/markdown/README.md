The Ultimate Markdown Guide: From Basics to Advanced
A complete, professional reference for writing clean, readable, and powerful Markdown. Use this guide to master syntax, avoid common pitfalls, and leverage advanced features.

1. Headings
Create hierarchical section headings using the hash/pound symbol (#). The number of # symbols corresponds to the heading level.

Syntax & Examples
markdown
# Heading Level 1 (H1)
## Heading Level 2 (H2)
### Heading Level 3 (H3)
#### Heading Level 4 (H4)
##### Heading Level 5 (H5)
###### Heading Level 6 (H6)
➤ Rendered Output:

Heading Level 1 (H1)
Heading Level 2 (H2)
Heading Level 3 (H3)
Heading Level 4 (H4)
Heading Level 5 (H5)
Heading Level 6 (H6)
Alternate Syntax (for H1 & H2)
For H1 and H2 only, you can use an alternate underline syntax.

markdown
Heading Level 1
===============

Heading Level 2
---------------
💡 Pro Tips & Knowledge
Automatic Correctness: The actual numbers you use in ordered lists don't matter. Markdown will automatically render them in the correct order. Writing 1. First, 1. Second, 1. Third will still output as 1. First, 2. Second, 3. Third.

Best Practice: Always put a space between the # and the heading text. # Like This not #NotThis.

Readability: Place a blank line before and after a heading to ensure it renders correctly across all platforms.

2. Paragraphs and Line Breaks
Paragraphs
To create paragraphs, separate one or more lines of text with one or more blank lines.

markdown
This is the first paragraph. I can write multiple sentences here and they will all form one coherent block.

This is the second paragraph. The blank line above is what creates the separation.
Line Breaks (Soft Returns)
To force a line break within the same paragraph (creating a <br> tag in HTML), end a line with two or more spaces and then press return.

markdown
This is the first line.⋅⋅
This is the second line, but it's still in the same paragraph.
💡 Pro Tips & Knowledge
The Two-Space Rule: This is one of Markdown's most common "gotchas." If your line breaks aren't appearing, you likely forgot the two trailing spaces.

Alternative: For maximum compatibility and clarity, you can use the HTML <br> tag directly if you find the two-space method invisible and confusing.

Don't Indent: Indenting paragraphs with spaces or tabs will turn them into code blocks, which is not what you want for regular text.

3. Emphasis (Bold and Italic)
Bold Text
Surround text with two asterisks (**) or two underscores (__).

markdown
I love **bold text**.
I love __bold text__.
➤ Rendered Output: I love bold text. I love bold text.

Italic Text
Surround text with one asterisk (*) or one underscore (_).

markdown
Italicized text is the *cat's meow*.
Italicized text is the _cat's meow_.
➤ Rendered Output: Italicized text is the cat's meow. Italicized text is the cat's meow.

Bold and Italic
Surround text with three asterisks (***) or three underscores (___).

markdown
This is ***really important*** text.
This is ___really important___ text.
➤ Rendered Output: This is really important text.

💡 Pro Tips & Knowledge
Asterisks vs. Underscores: Prefer using asterisks (*). They are more consistent and less likely to be confused with underscores in variable names (e.g., my_variable).

Mid-Word Emphasis: You can apply emphasis in the middle of a word, like un**believe**able.

Escaping: To type a literal * or _, escape it with a backslash: \*.

4. Blockquotes
Blockquotes are used to highlight quotes, excerpts, or side comments.

Basic Blockquote
Use the > character at the beginning of each line you want to quote.

markdown
> This is a single-line blockquote. It will be indented and styled differently.
➤ Rendered Output:

This is a single-line blockquote. It will be indented and styled differently.

Multiline & Nested Blockquotes
You can create multiline and nested blockquotes.

markdown
> This is the first level of quoting.
>
> > This is a nested blockquote. Very useful for conversations.
>
> Back to the first level.
Blockquotes with Other Elements
Blockquotes can contain other Markdown elements like headers, lists, and code.

markdown
> ## A Heading Inside a Quote
> - A list item.
> - Another item.
> `Code` looks like this.
💡 Pro Tips & Knowledge
Compatibility: Always place a blank line before and after a blockquote for clean rendering across all parsers.

5. Lists
Ordered (Numbered) Lists
Create an ordered list by using numbers followed by periods.

markdown
1. First item
2. Second item
3. Third item
    1. Indented item (4 spaces or 1 tab)
    2. Another indented item
4. Fourth item
➤ Rendered Output:

First item

Second item

Third item

Indented item

Another indented item

Fourth item

Unordered (Bulleted) Lists
Create an unordered list using hyphens (-), asterisks (*), or plus signs (+). Be consistent within the same list.

markdown
- First item
- Second item
- Third item
    - Indented item (4 spaces or 1 tab)
    - Another indented item
- Fourth item
➤ Rendered Output:

First item

Second item

Third item

Indented item

Another indented item

Fourth item

💡 Pro Tips & Knowledge
Numbering Magic: You can use 1. for every item. Markdown's output will automatically be correct numerically. This is great for when you are constantly reordering list items.

Indentation is Key: Use 4 spaces or 1 tab to indent items for nested lists. Using 2 or 3 spaces will break the structure on many platforms.

Starting with a Number: To start an unordered list item with a number (e.g., 1980. A great year), escape the period with a backslash: - 1980\. A great year. This prevents it from being parsed as an ordered list.

6. Code
Inline Code
Denote a word or phrase as code by wrapping it in single backticks (`).

markdown
Use the `printf()` function for debugging.
To include a literal backtick, use double backticks: `` `Code` ``
➤ Rendered Output:
Use the printf() function for debugging.
To include a literal backtick, use double backticks: Code

Code Blocks
For multi-line code, indent every line by at least 4 spaces or 1 tab.

markdown
    <html>
        <head>
            <title>Test</title>
        </head>
    </html>
➤ Rendered Output:

text
<html>
    <head>
        <title>Test</title>
    </head>
</html>
Fenced Code Blocks (Recommended)
The modern, easier way is to use "fenced" code blocks with triple backticks (```). You can also specify the language for syntax highlighting.

markdown
```python
def hello_world():
    print("Hello, World!") # This is Python code
```
➤ Rendered Output:

python
def hello_world():
    print("Hello, World!") # This is Python code
💡 Pro Tips & Knowledge
Fenced is Better: Fenced code blocks (using ```) are not part of the original Markdown spec but are supported by virtually all modern editors (VS Code, GitHub, GitLab). They are much easier to write and read than indented code blocks.

Syntax Highlighting: Specifying a language (e.g., python`,javascript`) after the opening ticks enables syntax highlighting, making your code far more readable.

7. Horizontal Rules
Create a thematic break (<hr>) by placing three or more hyphens (---), asterisks (***), or underscores (___) on a line by themselves.

markdown
Section 1 text.

---

Section 2 text.
➤ Rendered Output:
Section 1 text.

Section 2 text.

💡 Pro Tips & Knowledge
Best Practice: Place a blank line before and after the rule to ensure it is parsed correctly and doesn't get mistaken for a heading.

8. Links
Inline Links
The most common link style. The link text goes in [square brackets] and the URL goes in (parentheses).

markdown
My favorite search engine is [DuckDuckGo](https://duckduckgo.com).
Add a tooltip title: [Google](https://google.com "The Search Giant").
➤ Rendered Output:
My favorite search engine is DuckDuckGo.
Add a tooltip title: Google.

URLs and Email Addresses
To quickly turn a URL or email address into a link, wrap it in angle brackets.

markdown
<https://www.markdownguide.org>
<fake@example.com>
➤ Rendered Output:
https://www.markdownguide.org
fake@example.com

Reference-Style Links
Reference-style links separate the link text from the URL definition, making your source text much cleaner. This is ideal for academic papers or documents with many links.

Part 1 (In-text): Use a second set of brackets with a label.

markdown
Learn more about [Markdown][1] or see the [specification][spec].
Part 2 (Anywhere in the document, often at the bottom): Define the label.

markdown
[1]: https://www.markdownguide.org "The Markdown Guide"
[spec]: https://daringfireball.net/projects/markdown/ "Original Spec"
➤ Rendered Output:
Learn more about Markdown or see the specification.

💡 Pro Tips & Knowledge
Spaces Break URLs: URLs cannot contain spaces. If you need to link to a resource with a space in its path, you must use %20 (e.g., https://example.com/my%20page) or use an HTML <a> tag.

Clean Source Code: Use reference-style links in long documents to keep your paragraph text clean and manageable.

9. Images
The syntax for images is identical to links, but preceded by an exclamation mark (!).
![Alt Text](URL "Optional Title")

Alt Text: Essential for accessibility (screen readers) and SEO. Describe the image.

Title: Optional. Displayed as a tooltip on hover.

markdown
![The logo for Markdown: a red dot](https://markdown-here.com/img/icon256.png "Markdown Logo")
➤ Rendered Output:
https://markdown-here.com/img/icon256.png

Linking an Image
To make an image a clickable link, wrap the entire image syntax in [square brackets] and provide the link URL in (parentheses).

markdown
[![Markdown Logo](https://markdown-here.com/img/icon256.png)](https://daringfireball.net/projects/markdown/)
💡 Pro Tips & Knowledge
Always Use Alt Text: Never leave the alt text blank. It's crucial for accessibility and context if the image fails to load.

Sizing: Basic Markdown does not support image resizing. To control an image's dimensions, you must use the HTML <img> tag: <img src="image.jpg" alt="Alt Text" width="200">.

10. Advanced Features (Extended Syntax)
These features are not part of the original Markdown specification but are widely supported by platforms like GitHub, GitLab, and modern editors.

Tables
Create tables using pipes (|) and hyphens (-). Hyphens define the header row, and colons (:) set alignment.

markdown
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
| *Left*      | **Center**  | ~~Right~~     |
➤ Rendered Output:

Syntax	Description	Test Text
Header	Title	Here's this
Paragraph	Text	And more
Left	Center	~~Right~~
Task Lists
Create interactive checkboxes (perfect for READMEs and project notes).

markdown
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
➤ Rendered Output:

Write the press release

Update the website

Contact the media

Strikethrough
Wrap text with two tildes (~~) to cross it out.

markdown
This was ~~a mistake~~ an excellent idea.
➤ Rendered Output: This was ~~a mistake~~ an excellent idea.

💡 Pro Tips & Knowledge
Platform Support: Remember that these extended syntax features may not work everywhere. They are guaranteed to work on GitHub, GitLab, and in most modern code editors.

11. Escaping Characters
To display a literal character that has a special meaning in Markdown (like * or #), prefix it with a backslash (\).

markdown
\* This is a literal asterisk, not italic text.
\# This is a hash symbol, not a heading.
\\ This is a backslash.
➤ Rendered Output:
* This is a literal asterisk, not italic text.
# This is a hash symbol, not a heading.
\ This is a backslash.

Characters you can escape: \ `` * _ {} [] () # + - . ! |

Final Advice & Pro Tips
Preview is Your Best Friend: Always preview your Markdown (in VS Code, GitHub, StackEdit) to see how it will actually look. Different parsers can have slight variations.

When in Doubt, Use HTML: Markdown is a superset of HTML. If you can't achieve something with Markdown (like changing text color <span style="color:red">red</span> or embedding a video), just use the HTML tag. It will work perfectly.

Consistency is Key: Pick a style (e.g., - for lists, ** for bold) and stick with it throughout your document. It makes your source code cleaner and easier to maintain.

Learn Your Platform's Flavored Markdown: If you use GitHub/GitLab extensively, learn GitHub-Flavored Markdown (GFM). It includes powerful features like tables, task lists, and automatic linkification of URLs.

Happy Writing! With this guide, you're equipped to create beautifully formatted documentation, notes, blogs, and web content.

