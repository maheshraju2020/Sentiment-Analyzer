let rec = require("../home_page/recents.json");
let res = document.getElementById("result");
let cur = rec["recents"][0];
res.innerHTML = "Sentiment Analysis Results";
