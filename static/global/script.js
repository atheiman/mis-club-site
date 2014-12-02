// Restaurateur JavaScript
function renderMarkdownElements(elements) {
    elements = elements || document.getElementsByClassName('markdown-content');
    for (var i = 0; i < elements.length; i++) {
        elements[i].innerHTML = marked(elements[i].innerHTML);
    }
}
