const path = require("path");
// const { ipcMain } = require("electron");
// let message_changer = require("../loading_page/message_changer");

const getdata = (keyword, win, dir) => {
	try {
		console.log("idhar bhi aaya");
		var { PythonShell } = require("python-shell");
		var options = {
			scriptPath: path.join(__dirname, "../Tweet_extracter/"),
			args: [keyword]
		};

		let pyshell = new PythonShell("sentiment_handler.py", options);

		pyshell.on("message", message => {
			if (message == "error") {
				throw new Error();
			}
			// message_changer(message);
		});
		pyshell.on("close", () => {
			pathname = path.join(dir, "./analytics/analytics.html");
			win.loadURL(pathname);
		});
	} catch (e) {
		pathname = path.join(dir, "../error_page.html");
		win.loadURL(pathname);
	}
};
// getdata("s20");
exports.getdata = getdata;
