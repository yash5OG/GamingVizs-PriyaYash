// from data.js
var tableData = data;

// select the filter button
var button = d3.select("#filter-btn");

// select the body element
var tbody = d3.select("tbody");

// console.log(data);

// listing sightings in the table
data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    })
});

// taking  user input to filter by date
button.on("click",function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);

    // filter the data table to match user's input
    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);
    tbody.html("");

    // displayed filtered data
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        })
    });
});