function getbhkValue() {
    var uibhk = document.getElementsByName("uiBHK");
    for (var i in uibhk) {
        if (uibhk[i].checked) {
            return parseInt(i) +1;
        }
    }
    return -1;
}



function getBathroomValue() {
    var uiBathroom = document.getElementsByName("uiBathroom");
    for (var i in uiBathroom) {
        if (uiBathroom[i].checked) {
            return parseInt(i) +1;
        }
    }
    return -1;
}



function onClickedEstimateRent() {
    console.log("Estimated Rent button clicked");
    var size = document.getElementsByName("uisize");
    var bhk = getbhkValue();
    var bathroom = getBathroomValue();
    var city = document.getElementsByName("uiCity");
    var estRent = document.getElementsByName("uiEstimatedRent");

    var url = "http://127.0.0.1:5000/predict_house_rent";

    $.post(url, {
        size: parseInt(size.value),
        bhk: bhk,
        bathroom: bathroom,
        city: city.value
    }, function(data, status) {
        console.log(data.estimate_rent);
        estRent.innerHTML = "<h2>" + data.estimate_rent.toString() + "Lakh</h2>";
        console.log(status)
    });
}



function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names"
    var url = "/api/get_location_names";
    $.get(url, function(data, status){
        console.log("got response for get_location_names request");
        if(data) {
            var cities = data.cities;
            var uicity = document.getElementById("uicity");
            $('#uicity').empty();
            for (var i in cities) {
                var opt = new Option(cities[i]);
                $("#uicities").append(opt);
            }
        }
    });
}

window.onload = onPageLoad;