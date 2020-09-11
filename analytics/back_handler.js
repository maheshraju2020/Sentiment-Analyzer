document.querySelector(".back").addEventListener("click", e => {
	console.log("Aaya to hai");
	e.preventDefault();
	const { ipcRenderer } = require("electron");
	ipcRenderer.send("open-home");
});
