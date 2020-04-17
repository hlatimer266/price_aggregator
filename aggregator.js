var category = document.getElementById("category");
var brand = document.getElementById("brand");
var model = document.getElementById("model");

var tvs = ['Samsung', 'Visio', 'LG', 'Sony', 'TCL'];
var laptops = ['Apple', 'HP', 'Dell', 'Lenovo', 'ASUS'];
var monitors = ['HP', 'Dell', 'Acer', 'Lenovo', 'ASUS'];
var phones = ['Apple', 'Samsung', 'LG', 'Motorola', 'Google'];

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

category.addEventListener("change",function(){
	var choice = category.options[category.selectedIndex].value
	brand_options(choice);
});
