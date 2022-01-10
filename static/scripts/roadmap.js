function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}


let islands = document.getElementsByTagName('main')[0].getElementsByClassName('island-block')
for (let i = 0; i < islands.length; i++) {
    let island = islands[i]
    let height = island.clientHeight / 6
    island.style.marginTop = height * getRandomInt(4) + 'px'
}

