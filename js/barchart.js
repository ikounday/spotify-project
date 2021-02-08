d3.json("data/tracks.json", function(data) {
var color = ["#1db954a2"];

new d3plus.BarChart()
  .select("#bar")
  .groupPadding(20)
  // .groupBy("group")

  .shapeConfig({
    fill: function(d) {
      return color
    },
  })
  .config({
    data: data,

    discrete: "y",
    groupBy: "group",
    legend: false,
    // shapeConfig: {
    //   label: false
    // },
    x: "value",
    y: "group",
    xConfig: {
      barConfig: {
        "opacity": 0
      },
      gridConfig: {
        "opacity": 0
      },
      // labels: [],
      //     title: "Weelky Top 10 Popularity",
      //     titleConfig: {
      //   fontColor: "white"
      // },
      // shapeConfig: {
      //   labelConfig: {
      //     fontMin: 12,
      //     fontMax: 14,
      //     color: "white",
      //   }
      // },
      tickSize: 0
    },
    yConfig: {
      barConfig: {
        opacity: 0
      },
      labels: [],
      gridConfig: {
        opacity: 0
      },
    }
  })

  .tooltipConfig({
    body: function(d) {
      var table = "<table class='tooltip-table'>";
      // table += "<tr><td class='title'>" + d.id + "</td></tr>";
      table += "<tr><td class='title'>Popularity:</td><td class='data'>" + d.value + "</td></tr>";
      // table += "</table>";
      return table;
    },
    footer: function(d) {
      return "<sub class='tooltip-footer'>Data Collected in 03/02/2021</sub>";
    },
    tbody: function(d) {
      const table = [];
      return table;
    },
    title: function(d) {
      var txt = d.id;
      return txt.charAt(0).toUpperCase() + txt.substr(1).toUpperCase();;
    }
  })
  .render();
  });
