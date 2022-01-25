function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}


let islands = document.getElementsByTagName('main')[0].getElementsByClassName('island-block')
for (let i = 0; i < islands.length; i++) {
    let island = islands[i]
    let height = island.clientHeight / 6
    island.style.marginTop = height * getRandomInt(4) + 'px'
}

let descriptions = document.getElementsByTagName('main')[0].getElementsByClassName('descr')

for (let i = 0; i < islands.length; i++) {
    islands[i].addEventListener("mouseenter", {handleEvent: show_tip, ind: i});
    islands[i].addEventListener("mouseleave", {handleEvent: hide_tip, ind: i});
}

function show_tip() {
    let index = this.ind
    descriptions[index].style.display = "block";
}


function hide_tip() {
    let index = this.ind
    descriptions[index].style.display = "none";
}
