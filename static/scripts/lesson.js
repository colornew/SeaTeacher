let txt = ''
let count_block = 0
let first = true
let st = {}
let blockContent = document.getElementsByClassName('content')[0]
let text = blockContent.textContent;
blockContent.textContent = ''
let style_check = false
let cont = document.createElement('div')
let style = ''
for (let i = 0; i < text.length + 1; i++) {
    let char = text.charAt(i)
    if (char === '*') {
        if (first) {
            blockContent.appendChild(cont);
            cont = document.getElementsByClassName('content-block')[count_block]
            cont.innerHTML = txt
            count_block++
            cont = document.createElement('div')
            txt = ''
            cont.className = 'content-block'
            style_check = true
            first = false
            style = '"'
        } else {
            style = '{' + style + '"}'
            style_check = false
            first = true
            st = JSON.parse(style)
            for (let attribute in st) {
                alert(attribute)
                if (attribute === 'format') {
                    alert(st[attribute])
                    if (st[attribute] === 'txt') {
                        alert(st[attribute])
                        cont.className += ' txt'
                    }
                }
            }

        }
    } else if (style_check) {
        if (char === ':') {
            style = style + '"' + ':' + '"'
        } else if (char === ',') {
            style = style + '"' + ',' + '"'
        } else {
            style += char
        }
    } else {
        txt += char
    }
}