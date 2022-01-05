let txt = ''
let count_block = 0
let first = true
let st = {}
let blockContent = document.getElementsByClassName('content')[0]
let text = blockContent.textContent;
blockContent.textContent = ''
let style_check = false
let cont = document.createElement('div')
cont.className = 'content-block'
let style = ''
for (let i = 0; i < text.length + 1; i++) {
    let char = text.charAt(i)
    if (char === '*') {
        if (first) {
            blockContent.appendChild(cont);
            cont = document.getElementsByClassName('content-block')[count_block]
            cont.innerHTML = txt
            count_block++
            txt = ''
            style_check = true
            first = false
            style = '"'
        } else {
            style = '{' + style + '"}'
            style_check = false
            first = true
            st = JSON.parse(style)
            let attr = st.format
            if (attr === 'format') {
                    if (st[attr] === 'txt') {cont.className += ' txt'
                        cont = document.createElement('div')
                    }
                    else if (st[attr] === 'photo') {cont.className += ' photo'
                        cont = document.createElement('img')
                    }
                    else if (st[attr] === 'audio') {cont.className += ' audio'
                        cont = document.createElement('audio')
                    }
                    else if (st[attr] === 'video') {cont.className += ' video'
                        cont = document.createElement('video')
                    }
                    else {
                        cont = document.createElement('div')
                    }
                    cont.className = 'content-block'
                }
            for (let attribute in st) {
                if (attribute === 'size'){
                    if (st[attribute] === '1') {cont.className += ' small'}
                    else if (st[attribute] === '2') {cont.className += ' medium'}
                    else if (st[attribute] === '3') {cont.className += ' large'}
                }
                if (attribute === 'color'){
                    if (st[attribute] === 'blue') {cont.className += ' blue'}
                    else if (st[attribute] === 'red') {cont.className += ' red'}
                    else if (st[attribute] === 'green') {cont.className += ' green'}
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