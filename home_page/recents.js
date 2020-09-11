let res = require("./recents.json");
const removeElement = (div) => {
    child = document.getElementById(div);
    parent = document.getElementById("search");
    item = child.querySelector("span").innerHTML;
    parent.removeChild(child);
    rem_item(item);
};

const rem_item = (item) => {
    var { PythonShell } = require("python-shell");

    var options = {
        scriptPath: path.join(__dirname, "/"),
        args: ["remove", item],
    };

    let pyshell = new PythonShell("recents_json_editor.py", options);
    pyshell.on("message", (message) => {
        console.log(message);
    });
    pyshell.on("close", () => {
        console.log("item removed");
    });
};

function readfile(file) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                var obj = this.responseText;
                var recents = JSON.parse(obj)["recents"];
                if (recents.length === 0) {
                    recents = JSON.parse(obj)["old"];
                }
                recents.map((ele, index) => {
                    var iDiv = document.createElement("div");
                    iDiv.ondblclick = () => {
                        removeElement("item" + String(index));
                    };
                    iDiv.onclick = () => {
                        const { ipcRenderer } = require("electron");
                        ipcRenderer.send("open-loading", ele);
                    };
                    iDiv.id = "item" + String(index);
                    iDiv.className = "items";
                    var ispan = document.createElement("span");
                    ispan.innerHTML = ele;
                    iDiv.appendChild(ispan);
                    document.querySelector("#search").appendChild(iDiv);
                });
            }
        }
    };
    rawFile.send(null);
}
readfile("./recents.json");
