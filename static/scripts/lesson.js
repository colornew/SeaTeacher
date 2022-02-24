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
            if (txt !== '') {
                cont.innerHTML = txt
            }
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
            } else if (attr === 'photo') {
                cont = document.createElement("img");
                let value = "/static/images/curse/" + st.source
                cont.setAttribute('src', value);
                cont.className = 'photo'
                cont.className += ' content-block'
            } else if (attr === 'audio') {
                cont = document.createElement('audio')
                cont.className = 'audio'
                let value = "/static/audio/curse/" + st.source
                cont.controls = 'controls'
                cont.type = 'audio/mpeg'
                cont.setAttribute('src', value);
                cont.className += ' content-block'
            } else if (attr === 'video') {
                cont = document.createElement('video')
                cont.className = 'video content-block';
                let sourceMP4 = document.createElement("source");
                sourceMP4.type = "video/mp4";
                cont.controls = "controls";
                sourceMP4.src = "/static/video/curse/" + st.source;
                cont.appendChild(sourceMP4);
            } else if (st.format === 'list') {
                cont = document.createElement('ul');
                cont.className = 'list content-block';
                let list = st.list.split('.')
                for (let elem in list) {
                    let li = document.createElement('li');
                    li.setAttribute('class', 'item');
                    li.appendChild(document.createTextNode(list[elem]))
                    cont.appendChild(li);
                }
            } else {
                cont = document.createElement('div')
                cont.className += ' content-block'
            }
            count_block++
            for (let attribute in st) {
                if (attribute === 'size') {
                    if (st[attribute] === '1') {
                        cont.className += ' small'
                    } else if (st[attribute] === '2') {
                        cont.className += ' medium'
                    } else if (st[attribute] === '3') {
                        cont.className += ' large'
                    }
                } else if (attribute === 'color') {
                    if (st[attribute].charAt(0) === 'r' && st[attribute].charAt(1) === 'g') {
                        color = st.color.replaceAll('.', ',')
                    } else {
                        color = st.color
                    }
                    if (st.format === 'txt') {
                        cont.style.color = color
                    } else if (st.format === 'photo') {
                        cont.style.border += color
                    }
                } else if (attribute === 'font') {
                    if (st.format === 'txt') {
                        if (st.font === 'italic') {
                            cont.style.fontStyle = 'italic'
                        } else if (st.font === 'fat') {
                            cont.style.fontWeight = 'bold'
                        }
                    }
                }
            }
            blockContent.appendChild(cont)

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

let block = document.body.getElementsByClassName('test-button')[0]
let block_source = document.createElement('div')
block_source.appendChild(block)
block_source.setAttribute('class', 'button-block')
blockContent.appendChild(block_source)


let viewport_height = window.innerHeight;

blockContent.addEventListener('dblclick', myFunction)


function myFunction() {
    if (blockContent.className === 'content slideUp') {
        blockContent.className = 'content'
    }
    else {
        blockContent.className += " slideUp";
    }
}


