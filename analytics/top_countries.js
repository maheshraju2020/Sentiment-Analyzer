let tops = require("../Tweet_extracter/charts_data.json");
tops = tops["top_locs"];
let countries = [];
let percent = [];
let total = 0;

const get_percent = (num, denom) => {
	return ((num / denom) * 100).toFixed(2);
};

tops.map(value => {
	countries.push(value["name"]);
	percent.push(value["y"]);
	total += Number(value["y"]);
});
for (let i = 0; i < percent.length - 1; i++) {
	for (let j = i + 1; j < percent.length; j++) {
		if (percent[j] > percent[i]) {
			let temp1 = percent[j];
			let temp2 = countries[j];
			percent[j] = percent[i];
			countries[j] = countries[i];
			percent[i] = temp1;
			countries[i] = temp2;
		}
	}
}
let rem = 0;
for (let i = 0; i < percent.length; i++) {
	if (countries[i] == "others") {
		rem = i;
		break;
	}
}
countries.splice(rem, 1);
percent.splice(rem, 1);
let loop;
if (countries.length > 5) {
	loop = 5;
} else {
	loop = countries.length;
}

for (let i = 0; i < loop; i++) {
	var iDiv = document.createElement("div");
	iDiv.innerHTML = countries[i];
	iDiv.className = "lists";
	var ispan = document.createElement("span");
	ispan.innerHTML = get_percent(percent[i], total) + "%";
	ispan.className = "percent";
	iDiv.appendChild(ispan);
	document.querySelector("#countrylist").appendChild(iDiv);
}
