//fish starts at 0, repeat as long as fish is < 4, add another fish
//loops are weird
for (let fish = 0; fish < 4; fish++) {
    console.log(`fish ${fish}`);
}

//list for minibird images
const minibirds = [
    "RBGU.gif",
    "BBMA.gif",
];

//list for links
const links = [
    "/birds/sp/gulls/RBGU/",
    "/birds/sp/crows/BBMA/",
]

let length = minibirds.length;

function randomNumberUpTo(limit) {
    return Math.floor(Math.random() * limit);
}

let randomNumber = randomNumberUpTo(length);

//replace link
function replaceLink() {
    document.getElementById("gull-link").setAttribute('href', links[randomNumber]);
}
function replaceImage() {
    document.getElementById("gull").setAttribute('src', minibirds[randomNumber]);
}

replaceLink()
replaceImage()
