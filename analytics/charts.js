var CanvasJS = require("./canvasjs.min");
let data = require("../Tweet_extracter/charts_data.json");
window.onload = function() {
	for (let i = 0; i < data["spine"].length; i++) {
		data["spine"][i]["x"] = new Date(data["spine"][i]["x"]);
	}
	var piechart = new CanvasJS.Chart("piechart", {
		animationEnabled: true,
		legend: {
			cursor: "pointer",
			itemclick: explodePie
		},
		data: [
			{
				type: "pie",
				showInLegend: true,
				toolTipContent: "{name}: <strong>{y}%</strong>",
				indexLabel: "{name} - {y}%",
				dataPoints: data["pie"]
			}
		]
	});
	var interest_over_time = new CanvasJS.Chart("spinechart", {
		animationEnabled: true,
		axisY: {
			title: "Sentiment Recorded"
		},
		data: [
			{
				yValueFormatString: "#,### Units",
				xValueFormatString: "DD",
				type: "spline",
				dataPoints: data["spine"]
			}
		]
	});
	var multigraph = new CanvasJS.Chart("multigraph", {
		// exportEnabled: true,
		animationEnabled: true,
		subtitles: [
			{
				text: "Click Legend to Hide or Unhide Data Series"
			}
		],
		axisX: {
			title: "Days"
		},
		axisY: {
			title: "% of Sentiments",
			titleFontColor: "#4F81BC",
			lineColor: "#4F81BC",
			labelFontColor: "#4F81BC",
			tickColor: "#4F81BC"
		},
		toolTip: {
			shared: true
		},
		legend: {
			cursor: "pointer",
			itemclick: toggleDataSeries
		},
		data: [
			{
				type: "column",
				name: "Positive",
				showInLegend: true,
				yValueFormatString: "##.##",
				dataPoints: data["multi"]["bar1"]
			},
			{
				type: "column",
				name: "Neutral",
				showInLegend: true,
				yValueFormatString: "##.##",
				dataPoints: data["multi"]["bar2"]
			},
			{
				type: "column",
				name: "Negative",
				showInLegend: true,
				yValueFormatString: "##.##",
				dataPoints: data["multi"]["bar3"]
			}
		]
	});
	var doughnut = new CanvasJS.Chart("country", {
		exportFileName: "Doughnut Chart",
		animationEnabled: true,
		legend: {
			cursor: "pointer",
			itemclick: explodePie
		},
		data: [
			{
				type: "doughnut",
				innerRadius: 90,
				showInLegend: true,
				toolTipContent: "<b>{name}</b>: ${y} (#percent%)",
				indexLabel: "{name} - #percent%",
				dataPoints: data["top_locs"]
			}
		]
	});

	piechart.render();
	interest_over_time.render();
	multigraph.render();
	doughnut.render();
};
function explodePie(e) {
	if (
		typeof e.dataSeries.dataPoints[e.dataPointIndex].exploded === "undefined" ||
		!e.dataSeries.dataPoints[e.dataPointIndex].exploded
	) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();
}
function toggleDataSeries(e) {
	if (typeof e.dataSeries.visible === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else {
		e.dataSeries.visible = true;
	}
	e.chart.render();
}
