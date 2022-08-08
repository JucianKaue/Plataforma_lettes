function validate(tag) {
	let stag;
	let tp;
	let vr;
	try{
		stag = document.querySelector(`#${tag}`);
	}
	catch{
		stag = document.querySelector(`.${tag}`);
	}
	tp = stag.type;
	switch(tp) {
		case "email":
			vr = stag.checkValidity();
			break;
		case "cpf":
			vr = stag.value();
			break;
		default:
			return(false);
	}
	return(vr);
}