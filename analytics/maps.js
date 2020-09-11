// var anychart = require("anychart");
anychart.onDocumentReady(function() {
	// The data used in this sample can be obtained from the CDN
	// https://cdn.anychart.com/samples/maps-choropleth/world-women-suffrage-map/data.json
	anychart.data.loadJsonFile("../Tweet_extracter/maps.json", function(data) {
		anychart.palettes
			.distinctColors()
			.items([
				"#fff59d",
				"#fbc02d",
				"#ff8f00",
				"#ef6c00",
				"#bbdefb",
				"#90caf9",
				"#64b5f6",
				"#42a5f5",
				"#1e88e5",
				"#1976d2",
				"#1565c0",
				"#01579b",
				"#0097a7",
				"#00838f"
			]);
		// The data used in this sample can be obtained from the CDN
		// https://cdn.anychart.com/samples/maps-choropleth/world-women-suffrage-map/data.js
		var dataSet = anychart.data.set(data);

		map_data = dataSet.mapAs({ description: "description" });

		var map = anychart.map();

		// set map settings
		map
			.geoData("anychart.maps.world")
			.legend(false)
			.interactivity({ selectionMode: "none" });

		var series = map.choropleth(map_data);
		series.geoIdField("iso_a2").labels(false);
		series.hovered().fill("#455a64");
		var scale = anychart.scales.ordinalColor([
			{ less: 0.5 },
			{ from: 0.5, to: 1 },
			{ from: 1, to: 2 },
			{ from: 2, to: 4 },
			{ from: 4, to: 8 },
			{ from: 8, to: 16 },
			{ from: 16, to: 32 },
			{ greater: 32 }
		]);

		scale.colors([
			"#D6D9DB",
			"#9DCBF1",
			"#1A95F9",
			"#ECB057",
			"#FEAB44",
			"#FE9410",
			"#EF5E5E",
			"#FF0000"
		]);
		series.colorScale(scale);

		var colorRange = map.colorRange();
		colorRange
			.enabled(true)
			.padding([20, 0, 0, 0])
			.colorLineSize(5)
			.marker({ size: 7 });
		colorRange
			.ticks()
			.enabled(true)
			.stroke("3 #ffffff")
			.position("center")
			.length(20);
		colorRange
			.labels()
			.fontSize(10)
			.padding(0, 0, 0, 5)
			.format(function() {
				var range = this.colorRange;
				var name;
				if (isFinite(range.start + range.end)) {
					name = range.start + " - " + range.end;
				}
				return name;
			});

		map
			.tooltip()
			.useHtml(true)
			.format(function() {
				var span_for_description = "<span>";

				if (
					getDescription(this.id) != undefined &&
					getDescription(this.id) != ""
				)
					result =
						span_for_description + getDescription(this.id) + "</span></strong>";
				return result;
			});

		// create zoom controls
		var zoomController = anychart.ui.zoom();
		zoomController.render(map);

		// set container id for the chart
		map.container("container");
		// initiate chart drawing
		map.draw();
		function returnHtml(desc, value) {
			a = "<b>Contribution: " + String(Math.round(value)) + "%</b>";
			pos = "<b>Positve: " + String(Math.round(desc.pos)) + "%<b>";
			neu = "<b>Neutral: " + String(Math.round(desc.neu)) + "%<b>";
			neg = "<b>Negative: " + String(Math.round(desc.neg)) + "%<b>";
			brk = "<br/>";
			return a + brk + brk + pos + brk + neu + brk + neg;
		}
		function getDescription(id) {
			for (var i = 0; i < data.length; i++) {
				if (data[i].id == id)
					return returnHtml(data[i].description, data[i].value);
			}
		}
	});
});
