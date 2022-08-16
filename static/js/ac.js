pageData = {
	// "cadastro_de_curso"
	"nome_curso": '',
	"participantes_curso": '',
	"orientador_curso": '',

	// "cadastro_de_projeto"
	"nome_projeto": '',
	"participantes_projeto": '',
	"orientador_projeto": '',

	// "dados_gerais"
	"nome_input": '',
	"cpf_input": '',
	"telefone_input": '',
	"email_input": '',
	"resumo_input": '',

	// "formacao_profissional"
	"formacao_prof": '',
	//create_curso [popup]
	"complemento_textarea": '',

	// "atuacao"
	"area_atuacao_select": '',
	"emprego_input": '',
}

function saveDescription(where) {
	typeof(where) == "string"
	  ? pageData[where] = document.querySelector(`#${where}`).value
	  : where.forEach(el => {pageData[el] = document.querySelector(`#${el}`).value});
}

function passDescriptionToBD() {
	// Save description to database!
}