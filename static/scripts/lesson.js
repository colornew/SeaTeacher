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
blockContent.appendChild(cont)
let style = ''
for (let i = 0; i < text.length + 1; i++) {
    let char = text.charAt(i)
    if (char === '*') {
        if (first) {
            cont = document.getElementsByClassName('content-block')[count_block]
            cont.innerHTML = txt
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
            alert('Create')
            if (attr === 'txt') {
                cont = document.createElement('div')
                cont.className = 'txt'

            } else if (attr === 'photo') {
                cont = document.createElement('img')
                cont.className = 'photo'
                let value = "/static/images/curse/" + st.name
                cont.setAttribute('src', value);
            } else if (attr === 'audio') {
                cont = document.createElement('audio')
                cont.className = 'audio'

            } else if (attr === 'video') {
                cont = document.createElement('video')
                cont.className = 'video'

            } else {
                cont = document.createElement('div')
            }
            cont.className += ' content-block'

            for (let attribute in st) {
                if (attribute === 'size') {
                    if (st[attribute] === '1') {
                        cont.className += ' small'
                    } else if (st[attribute] === '2') {
                        cont.className += ' medium'
                    } else if (st[attribute] === '3') {
                        cont.className += ' large'
                    }
                }
                if (attribute === 'color') {
                    if (st[attribute] === 'blue') {
                        cont.className += ' blue'
                    } else if (st[attribute] === 'red') {
                        cont.className += ' red'
                    } else if (st[attribute] === 'green') {
                        cont.className += ' green'
                    }
                }
            }
            blockContent.appendChild(cont)
            count_block++
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