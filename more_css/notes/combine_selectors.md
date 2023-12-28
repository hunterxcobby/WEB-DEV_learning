Combining selectors in CSS allows for more specific and targeted styling. When selectors are combined, they should be read from right to left. The selector farthest to the right, just before the opening curly bracket, is known as the key selector, identifying the element to which styles will be applied. Any selector to the left of the key selector serves as a prequalifier.

For example:

**HTML:**
```html
<div class="hotdog">
  <p>...</p>
  <p>...</p>
  <p class="mustard">...</p>
</div>
```

**CSS:**
```css
.hotdog p {
  background: brown;
}
.hotdog p.mustard {
  background: yellow;
}
```

In the first selector, `.hotdog p`, the combination of a class selector (hotdog) and a type selector (p) targets paragraph elements within an element with the class hotdog. In the second selector, `.hotdog p.mustard`, two class selectors (hotdog and mustard) and one type selector (p) target paragraphs with the class mustard within an element with the class hotdog.

Spaces within selectors are crucial. A space between selectors implies a descendant relationship, while no space selects elements with both conditions. For example, `.hotdog p.mustard` selects paragraphs with the class mustard inside an element with the class hotdog, but `.hotdog.mustard` selects elements with both classes hotdog and mustard.

Reading combined selectors from right to left helps understand the intended target. Specificity weights are crucial when combining selectors. The specificity point value is calculated by counting each type of selector: ID selectors contribute 1 point in the first column, class selectors contribute 1 point in the second column, and type selectors contribute 1 point in the third column.

For instance, the selector `.hotdog p` has a specificity point value of 0-1-1, and `.hotdog p.mustard` has a value of 0-2-1. Higher specificity weights take precedence in the cascade. Monitoring specificity is vital to avoid unintended styling conflicts. As we explore more combined selectors, we'll see their power in action.