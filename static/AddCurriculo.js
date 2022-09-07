function AddCurso() {
    let cursos = document.getElementById('text_cursos')
    
    cursos.value += `${document.getElementById('nome_curso').value},${document.getElementById('descricao_curso').value},${document.getElementById('cargahoraria_curso').value},${document.getElementById('instituicao_curso').value}|`

    document.getElementById('nome_curso').value = ''
    document.getElementById('descricao_curso').value = ''
    document.getElementById('cargahoraria_curso').value = ''
    document.getElementById('instituicao_curso').value = ''

    document.getElementById('add_curso').style.display='none'
}

function AddProjectOnGoing() {
    let project = document.getElementById('text_projetosandamento')
    let form_project = document.getElementById('add_projeto_andamento')

    project.value += `
    ${document.getElementById('nome_projeto_andamento').value},
    ${document.getElementById('descricao_projeto_andamento').value},
    ${document.getElementById('cargahoraria_Projeto_andamento').value},
    ${document.getElementById('datainicio_Projeto_andamento').value}
    |`

    form_project.style.display='none'
}

function AddProjectComplete() {
    let project = document.getElementById('text_projetosfinalizados')
    let form_project = document.getElementById('add_projeto_finalizado')
    
    project.value += `
    ${document.getElementById('nome_projeto_concluido').value},
    ${document.getElementById('descricao_projeto_concluido').value},
    ${document.getElementById('cargahoraria_Projeto_concluido').value},
    ${document.getElementById('datainicio_Projeto_concluido').value},
    ${document.getElementById('datafim_Projeto_concluido').value},
    |`

    form_project.style.display='none'
}