function validate(type, value) {
	let vr = false;
	switch(type) {
		case 'e':
			vr = email.checkValidaty();
			break;
		case 'n':
			// code block
			break;
		default:
			return(false);
    }
    return(false);
}