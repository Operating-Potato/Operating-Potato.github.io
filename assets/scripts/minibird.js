//fish starts at 0, repeat as long as fish is < 4, add another fish
//loops are weird
for (let fish = 0; fish < 4; fish++) {
    console.log(`fish ${fish}`);
}

//list of available minibirds
const minibirds = [
    "RBGU",
    "BBMA2",
    "DCCO2",
];

let length = minibirds.length;

function randomNumberUpTo(limit) {
    return Math.floor(Math.random() * limit);
}

let randomNumber = randomNumberUpTo(length);

//replace link
function replaceLink() {
    let link = "/birds/sp/" + minibirds[randomNumber].slice(0, 4);
    document.getElementById("gull-link").setAttribute('href', link);
}
function replaceImage() {
    let image = "https://operating-potato.github.io/birds/assets/minibirds/" + minibirds[randomNumber] + ".gif";
    document.getElementById("gull").setAttribute('src', image);
}

replaceLink()
replaceImage()
