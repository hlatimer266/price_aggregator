var category = document.getElementById("category");
var brand = document.getElementById("brand");
var model = document.getElementById("model");

var tvs = ['Samsung', 'LG', 'Visio', 'TCL', 'Sony'];
var laptops = ['Acer', 'Apple', 'ASUS', 'HP', 'Lenovo'];
var monitors = ['acer','asus','dell', 'hp', 'lenovo'];
var phones = ['apple', 'google', 'lg', 'samsung'];
var categories = ['tv','laptop','monitor','cell_phone']

var tv_models = [['UN65NU6900FXZA', 'UN32M4500BFXZA', 'UN43TU7000FXZA', 'UN55TU8000FXZA', 'UN50TU8000FXZA'],['65UM6900PUA', 'LGOLED65CXPU ', 'OLED77C9PUB', '75SM9070PUA', 'OLED55GXPUA'],['V505-G9', 'V555-G1', 'V655-G9', 'M658-G1', 'P659-G1'],['50S425', '43S425', '65R625', '55R625', '75S425'],['XBR55A9G', 'XBR-65X950G', 'XBR77A9G', 'XBR43X800H', 'XBR85X850G']]
var monitor_models = [['V206HQL','V226HQL','V246HQL','B206HQL','B226WL'],['PB238Q','VE278Q','VG275Q','VP228HE','VW22AT'],['P2319H','P2419H','U2412M','U2419H','U2717D'],['K5A38AA','N223','P204','P274','Z27'],['E2054','P24q','T23d','s22e-19','t2224d']]
var laptop_models = [['AN515-54-54W2','CP315-1H-P8QY','AN515-54-51M5','AN517-51-56YW'],['MUHN2LL/A','MUHP2LL/A','MV962LL/A','MV912LL/A'],['MJ401TA-BM3N5','GA502DU-BR7N6','X512FA-BI7A','Q536FD-BI7T15'],['15-EC0013DX','11M-AP0013DX','14-DK0002DX','14-DA0012DX'],['81VS0001US','81Q9002GUS','81Q90041US','81TC000JUS']]
var phone_models = [['iphone11', 'iphone11Pro', 'iphonexr', 'iphonexsmax'], ['pixel3a', 'pixel3axl', 'pixel4', 'pixel4xl'], ['G8XThinQ', 'K40', 'stylo5', 'V40ThinQ'], ['galaxys10plus', 'galaxys20', 'galaxys20plus', 'galaxys20ultra']]

function brand_options(option){
	var length = brand.options.length;
	var brands;
	for (i = length-1; i >= 1; i--) {
 		brand.options[i] = null;
	}
	if (option == 1){
	    brands = tvs;
	}
	if (option == 2){
        brands = laptops;
	}
	if (option == 3){
	    brands = monitors;
	}
	if (option == 4){
	    brands = phones;
	}
	length = brands.length;
	for (i = 0; i < length; i++){
		var opt = document.createElement("option");
		opt.value = i;
		opt.text = brands[i];
		brand.add(opt, null);
	}
}

function update_models(option, category_choice){
	var length = model.options.length;
	var models;
	for (i = length-1; i >= 1; i--) {
 		model.options[i] = null;
	}
	if (category_choice == 1) {
	    models = tv_models;
	}
	if (category_choice == 3) {
	    models = monitor_models;
	}
	if (category_choice == 4) {
	    models = phone_models;
	}
	length = models[option].length;
    if (option >= 0){
        for (i = 0; i < length; i++){
            var opt = document.createElement("option");
            opt.value = i;
            opt.text = models[option][i];
            model.add(opt, null);
        }
    }
}

category.addEventListener("change",function(){
	var choice = category.options[category.selectedIndex].value;
	brand_options(choice);
});

brand.addEventListener("change",function(){
    var category_choice = category.options[category.selectedIndex].value;
	var choice = brand.options[brand.selectedIndex].value;
	update_models(choice, category_choice);
});

function price_page(){
	var category_index = category.options[category.selectedIndex].value;

	var brand = document.getElementById('brand');
	var brand_index = brand.value;

	var model = document.getElementById('model');
	var model_index = model.value;

	if (categories[category_index-1] == "monitor"){
		var query_parm = monitors[brand_index] + "/" + monitor_models[brand_index][model_index];
	}
	else if (categories[category_index-1] == "cell_phone") {
		var query_parm = phones[brand_index] + "/" + phone_models[brand_index][model_index];
	}
	else if (categories[category_index-1] == "tv") {
		var query_parm = phones[brand_index] + "/" + tv_models[brand_index][model_index];
	}

	console.log('/'+ categories[category_index-1] +'?parm='+ query_parm + '.json')

	window.location.href='/'+ categories[category_index-1] +'?parm='+ query_parm + '.json';

	event.preventDefault();
}