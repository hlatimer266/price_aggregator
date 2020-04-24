var category = document.getElementById("category");
var brand = document.getElementById("brand");
var model = document.getElementById("model");

var tvs = ['Samsung', 'Visio', 'LG', 'Sony', 'TCL'];
var laptops = ['Apple', 'HP', 'Dell', 'Lenovo', 'ASUS'];
var monitors = ['HP', 'Dell', 'Acer', 'Lenovo', 'ASUS'];
var phones = ['Apple', 'Samsung', 'LG', 'Motorola', 'Google'];

var tv_models = [['UN65NU6900FXZA', 'UN32M4500BFXZA', 'UN43TU7000FXZA', 'UN55TU8000FXZA', 'UN50TU8000FXZA'],['65UM6900PUA', 'OLED65CXPUA', 'OLED65C9PUA', '65SM9000PUA', '49SM8600PUA'],['V505-G9', 'V555-G1', 'V655-G9', 'M658-G1', 'P659-G1'],['50S425', '43S425', '65R625', '55R625', '75S425'],['XBR55A9G', 'XBR55A8G', 'XBR65X950G', 'XBR77A9G', 'XBR85X950G']]

function brand_options(option){
	var length = brand.options.length;
	for (i = length-1; i >= 1; i--) {
 		brand.options[i] = null;
	}	
	if (option == 1){
		for (i = 0; i < tvs.length; i++){
			var opt = document.createElement("option");
			opt.value = i;
			opt.text = tvs[i];
			brand.add(opt, null);
		}
	}
	if (option == 2){
		for (i = 0; i < laptops.length; i++){
			var opt = document.createElement("option");
			opt.value = i;
			opt.text = laptops[i];
			brand.add(opt, null);
		}
	}
	if (option == 3){
		for (i = 0; i < monitors.length; i++){
			var opt = document.createElement("option");
			opt.value = i;
			opt.text = monitors[i];
			brand.add(opt, null);
		}
	}
	if (option == 4){
		for (i = 0; i < phones.length; i++){
			var opt = document.createElement("option");
			opt.value = i;
			opt.text = phones[i];
			brand.add(opt, null);
		}
	}
}

function tv_options(option){
	var length = model.options.length;
	for (i = length-1; i >= 1; i--) {
 		model.options[i] = null;
	}
    if (option >= 0){
        for (i = 0; i < tv_models[option].length; i++){
            var opt = document.createElement("option");
            opt.value = i;
            opt.text = tv_models[option][i];
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
	if (category_choice == 1){
	    tv_options(choice);
	}
});