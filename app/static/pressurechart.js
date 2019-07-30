var ctx = document.getElementById("pressureChart").getContext('2d');

var gradientStroke = ctx.createLinearGradient(0, 400, 0, 0);

gradientStroke.addColorStop(0,"rgb(128,0,255)");
gradientStroke.addColorStop(0.2,"rgb(0,0,255)");
gradientStroke.addColorStop(0.3,"rgb(100,255,255)");
gradientStroke.addColorStop(0.4,"rgb(220,255,255)");
gradientStroke.addColorStop(0.57,"rgb(255,255,0)");
gradientStroke.addColorStop(0.8,"rgb(255,0,0)");

var x = labels;
var y = values;
var set = [x,y];
var data = {
	labels: x,
	datasets: [{
		data: y,
		backgroundColor: gradientStroke
	}]
};
var options = { };
var	tempChart = new Chart(ctx, {
	type: 'bar',
	data: data,
	options: {
		scales: {
			xAxes: [{
				type: 'time',
				displayFormats: {
					second: 'HH:mm:ss',
					minute: 'HH:mm',
					hour: 'MMM D, H[h]'
				}
			}],
			yAxes: [{
				ticks: {
					min: 930,
					max: 1070,
					stepSize: 5
				}
			}]		
		}
	}		
});
