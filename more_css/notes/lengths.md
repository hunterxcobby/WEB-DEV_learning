
### Absolute Lengths
1. **Pixels (px):** Pixels are a common absolute unit and are often used for fixed-size elements. For example, setting the font size of paragraphs to 14 pixels: 
    ```css
    p {
      font-size: 14px;
    }
    ```

### Relative Lengths
1. **Percentages (%):** Percentages are relative to the length of another object. For instance, setting the width of an element to 50% of its parent's width:
    ```css
    .col {
      width: 50%;
    }
    ```
   Percentages are particularly useful in creating responsive designs.

2. **Em Units (em):** Em units are relative to the font size of an element. If an element has a font size of 14 pixels, setting its width to 5em would make it 70 pixels wide.
    ```css
    .banner {
      font-size: 14px;
      width: 5em;
    }
    ```
   Em units are commonly used for text-related styling, such as font sizes and spacing.

These units offer flexibility in designing layouts and styling elements, catering to the responsive nature of modern web design. While there are more units available, pixels, percentages, and em units are the most commonly used and a good starting point for understanding length values in CSS.