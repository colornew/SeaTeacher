let txt = ''
let count_block = 0
let count = 0
let first = true
let blockContent = document.getElementsByClassName('content')[0]
let text = blockContent.textContent;
let style_check = false
let style = ''
for (let i = 0; i < text.length + 1; i++) {
    let cont = document.createElement('div')
    let char = text.charAt(i)
    if (char === '*') {
        if (first) {
            cont.className = "content-block"
            blockContent.appendChild(cont);
            cont = document.getElementsByClassName('content-block')[count_block]
            cont.innerHTML = txt
            count_block++
            txt = ''
            style_check = true
            first = false
        }
        else {
            style_check = false
            first = true
        }
    }
    if (style_check) {

        count++
    }
}