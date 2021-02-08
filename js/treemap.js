d3.json("data/artists.json", function(data) {

    // console.log(data);
    new d3plus.Treemap()
      .data(data)
      .groupBy("id")
      .select("#tree")
      .shapeConfig({
        backgroundImage: function(d) {
          return d.image;
        },
        fill: function(d) {
          return d.color;
        },
        label: false,
      })
      .tooltipConfig({
        body: function(d) {
          var table = "<table class='tooltip-table'>";
          table += "<tr><td class='title'>" + d.id + "</td></tr>";
          // table += "<tr><td class='title'>Value:</td><td class='data'>" + d.value + "</td></tr>";
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
          var txt = d.rank;
          return txt.charAt(0).toUpperCase() + txt.substr(1).toUpperCase();;
        }
      })
      .render();
});
