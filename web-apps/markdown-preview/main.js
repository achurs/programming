import './style.css'

$(document).ready(function () {
const defaultText = `
# Header
## Sub-Header
[Link](https://example.com)
\`inline code\`
\`\`\`
// Code block
console.log("Hello, World!");
\`\`\`
- List item
> Blockquote
![Image](https://example.com/image.jpg)
**Bolded text**
`;
  $("#editor").val(defaultText)
  $("#preview").html(marked(defaultText))
  $("#editor").keyup(function () {
    $("#preview").html(marked($("#editor").val()))
  })
})

setupCounter(document.querySelector('#counter'))
