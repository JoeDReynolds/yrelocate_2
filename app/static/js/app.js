
// define the defalt & global  variable 
var buy=false;
 var rent=false;
 var markers=[];
var group={};
var schoolmarkers=[];
var schoolgroup={};
var housemarkers=[];
var group3={};
var zipcode=[];
var customOptions =
   {
   'maxWidth': '500',
   'className' : 'custom'
   };  
   //  #####################*******************************************************************************************************
//  city dropdown 
// function for dropdwon changed values: 
function getData(dataset) {
  // check remove  school markers if client choose school first 
  if (schoolmarkers.length>0){ 
    myMap.removeLayer(schoolgroup)
  }
  // ramove markers for housedata if it excits 
  if (housemarkers.length>0){ 
    myMap.removeLayer(group3)
  }
   // check if map has markers of cities  and then remove and add the new one. 
  if (markers.length>0){
    myMap.removeLayer(group)
  }
  // switch data for city.
  switch (dataset) {
  case "Austin":
  // ****** make pictures as icone of markers when the client chose Austin
  markers=[];
  for(var i=0;i< Austinphotos.length; i++){
      var picture=L.icon({
        iconUrl:Austinphotos[i].url,
        iconSize: [50, 50], // size of the icon
        popupAnchor: [0,-15]
        })
    var customPopup= `${Austinphotos[i].name }<br/><img src= ${Austinphotos[i].url} width='350px'/>`
      markers.push(
        L.marker(Austinphotos[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
      )
    } 
    // set Timeout Function to move for Austin 
    setTimeout(function () {
      group = L.featureGroup(markers).addTo(myMap);
      console.log( typeof group);
      myMap.fitBounds(group.getBounds());
    }, 500);
    break;

  case "Dallas":
    // ****** make pictures as icone of markers when the client chose Dallas

  markers=[];
  for(var i=0;i< Dallasphoto.length; i++){
      var picture=L.icon({
        iconUrl:Dallasphoto[i].url,
        iconSize: [50, 50], // size of the icon
        popupAnchor: [0,-15]
        })
    var customPopup= `${Dallasphoto[i].name }<br/><img src= ${Dallasphoto[i].url} width='350px'/>`
      markers.push(
        L.marker(Dallasphoto[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
      )
    } 
    // set Timeout Function to move for Dallas 
    setTimeout(function () {
      group = L.featureGroup(markers).addTo(myMap);
      myMap.fitBounds(group.getBounds());
    }, 500);

    break;
      // ****** make pictures as icone of markers when the client chose Houston

  case "Houston":
  markers=[];
  for(var i=0;i< Houstonphotos.length; i++){
      var picture=L.icon({
        iconUrl:Houstonphotos[i].url,
        iconSize: [50, 50], // size of the icon
        popupAnchor: [0,-15]
        })
    var customPopup= `${Houstonphotos[i].name }<br/><img src= ${Houstonphotos[i].url} width='350px'/>`
      markers.push(
        L.marker(Houstonphotos[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
      )
    }
    // set Timeout Function to move for houston 
    setTimeout(function () {
      group =  L.featureGroup(markers).addTo(myMap);
      myMap.fitBounds(group.getBounds());
    }, 500);
  
    break;
  }
}

// *****************************************************************************************************************
// code for housing Type part:
// take housing data in to the function : 
var housing= d3.json("/housing").then(successHandle);
function successHandle(result){
  housing=result 
  console.log(housing)
}
function errorHandle(error){
  console.log(error)
} 
// Dropdown for buy or rent :
function optionchenged(data) {
  // remove marker of housing  on map when they want to chenge rent or buy 
  if (housemarkers.length>0){ 
    myMap.removeLayer(group3)
  }
  console.log(data)
  switch (data) {
  case "Buy":

  buy =true;
  rent=false;
  alert( "200,000 to up ");

    break;
  case "Rent":

  alert( " price is for one_bedroom: 900 -1500$ ");
  rent =  true;
  buy=false;

    break;
  }
}

//  ####### ********************School Data **********************************#############################

function getschoolData(school) {
  // emove cities markers 
  myMap.removeLayer(group)
  // remove excisted school markers 
  if (schoolmarkers.length>0){ 
    myMap.removeLayer(schoolgroup)
  }
  console.log(school)
  switch (school) {
    // define markers for Middle school data. 
  case "Middle":
  d3.json("/middleschool").then(successHandle1);
  function successHandle1(result){
    var middle=result ;
    console.log(`middle data ${middle}`);
    schoolmarkers=[];
    console.log(`middle is ${middle.length}`);
    var middle1 = middle.filter(function(item) {
      return  item.display_name.includes("Austin");     
    });

    for(var i=0;i< middle1.length; i++){
        var picture=L.icon({
          iconUrl:"https://img.freepik.com/free-icon/students-cap_318-62709.jpg?size=338c&ext=jpg",
          iconSize: [30, 30], // size of the icon
          popupAnchor: [0,-15]
          })
      var customPopup= `Name: ${middle1[i].display_name }<br/> Rank of State:  ${middle1[i].state_Rank }<br/> Reginal_Rank:  ${middle1[i].reginal_rank}`
      schoolmarkers.push(
          L.marker(middle1[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
        )
      }
      setTimeout(function () {
        schoolgroup =  L.featureGroup(schoolmarkers).addTo(myMap);
        myMap.fitBounds(schoolgroup.getBounds());
      }, 500);
}
function errorHandle1(error){
  console.log(error)
} 
    break;
// define markers for Elementary school data. 
  case "Elementary":
  d3.json("/elementary").then(successHandle2);
  function successHandle2(result){
    var elementary=result ;
    console.log(`heloo maraym is ${elementary}`);
    schoolmarkers=[];
    var elementary1 = elementary.filter(function(item) {
      return  item.display_name.includes("Austin");     
    });

    for(var i=0;i< elementary1.length; i++){
        var picture=L.icon({
          iconUrl:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpFIYgN2Q-TzVhbfw1JWZUvS4h6AEvMuhj3gJttjDzu25Df30Y",
          iconSize: [30, 30], // size of the icon
          popupAnchor: [0,-15]
          })
      var customPopup= `Name: ${elementary1[i].display_name }<br/> Rank of State:  ${elementary1[i].state_Rank }<br/>Reginal_Rank:  ${elementary1[i].reginal_rank}`
      schoolmarkers.push(
          L.marker(elementary1[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
        )
      }
      setTimeout(function () {
        schoolgroup =  L.featureGroup(schoolmarkers).addTo(myMap);
        myMap.fitBounds(schoolgroup.getBounds());
      }, 500);
    
  }
  function errorHandle2(error){
    console.log(error)
  } 
    break;
// define markers for highschool school data. 

  case "High":
  d3.json("/highschool").then(successHandle3);
  function successHandle3(result){
    var highschool=result ;
    console.log(`heloo maraym is ${highschool}`);
    schoolmarkers=[];
    var highschool1 = highschool.filter(function(item) {
      return  item.display_name.includes("Austin");     
    });

    for(var i=0;i< highschool1.length; i++){
        var picture=L.icon({
          iconUrl:"data:image/jpeg;base64,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",
          iconSize: [30, 30], // size of the icon
          popupAnchor: [0,-15]
          })
      var customPopup= `Name: ${highschool1[i].display_name }<br/> Rank of State:  ${highschool1[i].state_Rank }<br/>Reginal_Rank:  ${highschool1[i].reginal_rank}`
      schoolmarkers.push(
          L.marker(highschool1[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
        )
      }
      setTimeout(function () {
        schoolgroup =  L.featureGroup(schoolmarkers).addTo(myMap);
        myMap.fitBounds(schoolgroup.getBounds());
      }, 500);
    
  }
  function errorHandle3(error){
    console.log(error)
  } 
    break;
  }
}
// ###################*********************************filter part *********************#################################
// function for submit buttton . 
$ ("#filter").on("click",handlecheck)
function handlecheck(){
  myMap.removeLayer(group)
  // check if map has markers and then remove and add the new one.
  if (housemarkers.length>0){
    myMap.removeLayer(group3)
  };
  // put value of input box in filter variable
  var filter = parseInt(document.getElementById("price").value);
  // if buy is true then filter data base on house price and else rent price and make house map array 
  if (buy ){
    var housemap = housing.filter(function(item) {
      return item.AveHomePrice < filter && item.display_name.includes("USA") ;
      
    });
    console.log("i am in buy")
  }
  else{
    var housemap=housing.filter(function(item) {
      return item.AveRentPrice < filter && item.display_name.includes("USA"); 
      
    });
    console.log("i am in rent")
  }
// make house markers base on housemap array(filter data)
  housemarkers=[];
  for(var i=0;i< housemap.length; i++){
    // define icone for map.
    var picture=L.icon({
      iconUrl:"https://cdn1.iconfinder.com/data/icons/engineers7/102/Untitled-28-512.png",
      iconSize: [30, 30], // size of the icon
      popupAnchor: [0,-15]
      })
    var customPopup= `Address: ${housemap[i].display_name }<br/>  Avarage Home Price: ${housemap[i].AveHomePrice }$ <br/> Avarage Rent Price(one_bedroom):${housemap[i].AveRentPrice }$ `
    housemarkers.push(
        L.marker(housemap[i].coordinates, {icon: picture}).bindPopup(customPopup,customOptions)
      )
  }
  // set timeout function to get the bounds. 
    setTimeout(function () {
      group3 =  L.featureGroup(housemarkers).addTo(myMap);
      myMap.fitBounds(group3.getBounds());
    }, 500);
};





