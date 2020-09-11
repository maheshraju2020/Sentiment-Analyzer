var xmlhttp = new XMLHttpRequest();
var theUrl = "./recents.json";
xmlhttp.open("POST", theUrl);
xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xmlhttp.send(
	JSON.stringify({ email: "hello@user.com", response: { name: "Tester" } })
);
