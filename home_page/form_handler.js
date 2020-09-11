let form = document.querySelector("form");
const path = require("path");

form.addEventListener("submit", e => {
	e.preventDefault();
	let data = document.getElementById("data").value;
	console.log(data);
	document.getElementById("data").value = "";
	// recents["recents"].unshift(data);
	add_data(data);
	const { ipcRenderer } = require("electron");
	ipcRenderer.send("open-loading", data);
});

const add_data = item => {
	var { PythonShell } = require("python-shell");

	var options = {
		scriptPath: path.join(__dirname, "/"),
		args: ["add", item]
	};

	let pyshell = new PythonShell("recents_json_editor.py", options);
	pyshell.on("message", message => {
		console.log(message, "lol");
	});
	pyshell.on("close", () => {
		console.log("item added");
	});
};

module.add_data = add_data;
