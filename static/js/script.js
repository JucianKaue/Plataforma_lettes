/* EMAIL
* <input id='a' type="email" name="email">
* <button id="bt" onclick="alert(validate('a'));">Ver</button>
*/

/* CPF
* <input id="abc" type="cpf" name="{{ type }}" maxlength="14" onkeyup="formatcpf('[#] {{ id }}')">
* <button onclick="alert(validate(' {{ input[id] }} '));">text</button>
*/

function formatcpf(tag) {
	let stag;
	if(tag.charAt(0) != ('#') && tag.charAt(0) != ('.')) {
		try{
			stag = document.querySelector(`#${tag}`);
		}
		catch{
			stag = document.querySelector(`.${tag}`);
		}
	}
	else{
		stag = document.querySelector(tag);
	}
	if(stag.value.length == 3 || stag.value.length == 7) {
		stag.value += '.';
	}
	else if(stag.value.length == 11) {
		stag.value += '-';
	}
}

function validate(tag) {
	let stag;
	let tp;
	let val;
	if(tag.charAt(0) != ('#') && tag.charAt(0) != ('.')) {
		try{
			stag = document.querySelector(`#${tag}`);
		}
		catch{
			stag = document.querySelector(`.${tag}`);
		}
	}
	else{
		stag = document.querySelector(tag);
	}
	val = stag.value;
	tp = stag.name.toLowerCase();
	switch(tp) {
		case "email":
			return(stag.checkValidity());
			break;
		case "cpf":
			val = val.replace(/[^\d]+/g,'');
			let sum = 0;
			let rest = 0;
			for(let n = 0; n <= 9; n++){
				let re = new RegExp(`^${n}+$`);
				if(re.test(val)){
					return false;
				}
			}
			for(i = 1; i <= 9; i++){
				sum += parseInt(val.substring(i-1,i)) * (11 - i);
			}
			rest = (sum * 10) % 11;
			if((rest == 10) || (rest == 11)) {
				rest = 0;
			}
			if(rest != parseInt(val.substring(9,10))) {
				return false;
			}
			sum = 0;
			for(i = 1; i <= 10; i++) {
				sum += parseInt(val.substring(i-1,i)) * (12 - i);
			}
			rest = (sum * 10) % 11;
			if((rest == 10) || (rest == 11)) {
				rest = 0;
			}
			if(rest != parseInt(val.substring(10,11))){
				return false;
			}
			return true;
			break;
	}
}