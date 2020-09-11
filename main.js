const electron = require("electron");
const url = require("url");
const path = require("path");
const { app, BrowserWindow, ipcMain } = electron;
let homePage;
try {
	// require("electron-reload")(__dirname, {
	// 	electron: require(`${__dirname}/node_modules/electron`)
	// });

	app.on("ready", () => {
		homePage = new BrowserWindow({
			webPreferences: {
				nodeIntegration: true
			}
		});
		homePage.setMenu(null);
		homePage.setMinimumSize(700, 400);
		// homePage.webContents.openDevTools();

		homePage.loadURL(
			url.format({
				pathname: path.join(__dirname, "/home_page/index.html"),
				protocol: "file",
				slashes: true
			})
		);

		ipcMain.on("open-loading", (event, keyword) => {
			pathname = path.join(__dirname, "./loading_page/loading_page.html");
			homePage.loadURL(pathname);
			let { getdata } = require("./linkers/getdata.js");
			getdata(keyword, homePage, __dirname);
		});

		ipcMain.on("open-analytics", (event, args) => {
			pathname = path.join(__dirname, "./analytics/analytics.html");
			homePage.loadURL(pathname);
		});

		ipcMain.on("open-home", event => {
			pathname = path.join(__dirname, "/home_page/index.html");
			homePage.loadURL(pathname);
		});
	});
} catch {
	pathname = path.join(__dirname, "/home_page/index.html");
	homePage.loadURL(pathname);
}
