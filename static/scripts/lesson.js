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
let color;
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
            if (attr === 'txt') {
                cont = document.createElement('div')
                cont.className = 'txt'
                cont.className += ' content-block'
                blockContent.appendChild(cont)
            } else if (attr === 'photo') {
                let sourcePhoto = document.createElement("img");
                let value = "/static/images/curse/" + st.source
                sourcePhoto.setAttribute('src', value);
                sourcePhoto.className = 'photo'
                sourcePhoto.className += ' content-block'
                blockContent.appendChild(sourcePhoto)
            } else if (attr === 'audio') {
                cont = document.createElement('audio')
                cont.className = 'audio'
                let value = "/static/audio/curse/" + st.source
                cont.controls = 'controls'
                cont.type = 'audio/mpeg'
                cont.setAttribute('src', value);
                cont.className += ' content-block'
                blockContent.appendChild(cont)
            } else if (attr === 'video') {
                cont = document.createElement('video')
                cont.className = 'video'
                cont.className += ' content-block'
                blockContent.appendChild(cont)
                let sourceMP4 = document.createElement("source");
                sourceMP4.type = "video/mp4";
                sourceMP4.src = "/static/video/curse/" + st.source;
                cont.appendChild(sourceMP4);
            } else {
                cont = document.createElement('div')
                cont.className += ' content-block'
                blockContent.appendChild(cont)
            }
            if (i !== 0){count_block++}
            cont = document.getElementsByClassName('content-block')[count_block]
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
                    if (st[attribute].charAt(0) === 'r' && st[attribute].charAt(1) === 'g') {
                        color = st.color.replaceAll('.', ',')
                        if (st.format === 'txt') {cont.style.color = color}
                        else if (st.format === 'photo'){
                            cont.style.border += color
                        }
                    } else {
                        cont.style.color = st.color
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