
// color homes 
var house1 = document.getElementById('house1');
var house2 = document.getElementById('house2');
var house3= document.getElementById('house3');
var house4= document.getElementById('house4');
var house5= document.getElementById('house5');
var house6= document.getElementById('house6');
var house7= document.getElementById('house7');
var house8= document.getElementById('house8');
var house9= document.getElementById('house9');
var house10= document.getElementById('house10');
var house11= document.getElementById('house11');
var house12= document.getElementById('house12');
var house13= document.getElementById('house13');
var house14= document.getElementById('house14');
var house15= document.getElementById('house15');
var house16= document.getElementById('house16');
var house17= document.getElementById('house17');

var homes = [house1,house2,house3,house4,house5,house6,house7,house8,house9,house10,house11,house12,house13,house14,house15,house16,house17]

// get values for wind Turbine slider  and update calcuation 
var slider = document.getElementById("myRange");
console.log(slider)
var output = document.getElementById("demo");
output.innerHTML = slider.value;
var windspeed=Number(slider.value);

slider.oninput = function() {
  output.innerHTML = this.value;
  windspeed=this.value
  console.log(windspeed)
  calculate()
}

//  get value for cp and update calculation 
var slider3 = document.getElementById("cprange");
var output3= document.getElementById("cpndemo");
output3.innerHTML = slider3.value;
var powercoff=Number(slider3.value);

slider3.oninput = function() {
  output3.innerHTML = this.value;
  powercoff=this.value;
  calculate()

}

//  get value for Electro and update calculation 
var slider4 = document.getElementById("Erange");
var output4= document.getElementById("Edemo");
output4.innerHTML = slider4.value;
var mechanicaEff=Number(slider4.value)

slider4.oninput = function() {
  output4.innerHTML = this.value;
  mechanicaEff=this.value;
  calculate()
}

//  function value chabed for daimotor to update calculation 

function inputchenged() {
  // RotorDiameter=Number(document.getElementById("diameter").value)
  calculate()
}
//  function value chabed for density to update calculation 
function densitychenged() {
  // RotorDiameter=Number(document.getElementById("diameter").value)
  calculate()
}

// write function to calculate data for Turbin power:
// ************************
// document.getElementById("mytext").value = "My value";

function calculate(){
  for (var i = 0; i < 17; i++) {
    homes[i].style.color = 'white';
  }
  var RotorDiameter=Number(document.getElementById("diameter").value)
  var AirDensiry= Number(document.getElementById("Aden").value)
  var SArea = RotorDiameter * RotorDiameter * Math.PI / 4
  console.log(SArea)
  console.log("hgdgdd",windspeed)
  var windpower=AirDensiry /2 *  SArea * windspeed*windspeed*windspeed/1000
  console.log(windpower)
  var EstimatedOut = windpower * powercoff * mechanicaEff/100;
  console.log(EstimatedOut)
  var Turbinpower = Math.round(EstimatedOut);
  console.log("turbin", Turbinpower)
  document.getElementById("TPower").value = Turbinpower;
  var Anpower = EstimatedOut * 8784 /1000;
  var Anualpower = Anpower.toFixed(2);
  document.getElementById("ATpower").value = Anualpower;
  var AverageCons=18000
  var Houses = Anualpower / AverageCons *1000 ;
  var HousesCut = Math.round(Houses);
  document.getElementById("houses").value = HousesCut;
  var housesPowered = Math.floor(Houses/225);
  console.log(housesPowered)
  if (HousesCut <= 100) {
    housesPowered = 1;
  }else if (HousesCut <= 200){
    housesPowered = 2;
  }else if (HousesCut <= 300){
    housesPowered = 3;
  }
  for (var i = 0; i < housesPowered; i++) {
    homes[i].style.color = 'yellow';
  }

}

function populatdroodown(){
  var path = "static/Data.csv";
  var path2="static/Data2.csv"
  d3.csv(path2).then(sucseefulhandel, errorhandel);
  function sucseefulhandel(data){
  var selector= d3.select("#searchby")
  console.log(data[0].cityName)
  data.forEach((info)=>{
    selector.append("option").text(info.cityName).property("value",data.cityName)
  })
}
// for another data method 
  // data.forEach((row)=>{
  //   selector.append("option").text(row.cityName).property("value",row.cityName)
  //   console.log(row.cityName)
  // })
  // }

  function errorhandel(error){
    console.log(error)
  }
}

function getData(name){
  // var path = "static/Data.csv";
  var path2="static/Data2.csv"
  d3.csv(path2).then(sucseefulhandel, errorhandel);
  function sucseefulhandel(data){
    var filterdata=data.filter(item=> item.cityName===name)
    var cityrow=filterdata[0]
    console.log( "gjhvhcv",cityrow.windspeed)
    d3.select("#myRange").property("value",cityrow.windspeed)
    console.log(slider.value)
    // output.innerHTML = slider.value;
    output.innerHTML=cityrow.windspeed;
    windspeed=Number(cityrow.windspeed)
    calculate()

    
// this is for another data method 
    // console.log(data)
  //   var filterdata=data.filter(row=>row.cityName===name)
  //   var cityrow=filterdata[0]
  //   d3.select("#myRange").property("value",cityrow.winds)
  //   output.innerHTML = slider.value;

  // console.log(cityrow.winds)
  // console.log(data)
  }

  function errorhandel(error){
    console.log(error)
  }
  

}
populatdroodown()
calculate()

