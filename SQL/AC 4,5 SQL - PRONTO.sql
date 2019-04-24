USE ac45

CREATE TABLE Usuario(
	IDUser int identity(1,1)
	,login_usuario varchar(25) not null
	,senha varchar(20) not null
	,dtExpiracao date not null
	,CONSTRAINT pkIDUser primary key(IDUser)
	,CONSTRAINT uq_login unique(login_usuario)  
)
CREATE TABLE Coordenador(
	IDCoordenador int identity(1,1)
	,IDUser int not null
	,nome varchar(60) not null
	,emailCoordenador varchar(60) not null
	,celularCoordenador varchar(9) not null
	,CONSTRAINT pkCoordenador primary key(IDCoordenador)
	,CONSTRAINT uqEmailCoord unique(emailCoordenador)
	,CONSTRAINT uqCelCoord unique(celularCoordenador)
	,CONSTRAINT fkUserInCoord foreign key(IDUser) references Usuario(IDUser)
)
CREATE TABLE Aluno(
	IDAluno int identity(1,1)
	,IDUser int not null
	,nome varchar (60) not null
	,emailAluno varchar(60) not null
	,celularAluno varchar(9) not null
	,CONSTRAINT pkAluno primary key(IDAluno)
	,CONSTRAINT uqEmailAluno unique(emailAluno)
	,CONSTRAINT uqCelAluno unique(celularAluno)
	,CONSTRAINT fkUserInAluno foreign key(IDUser) references Usuario(IDUser)
)
CREATE TABLE Professor(
	IDProfessor int identity (1,1)
	,IDUser int not null
	,emailProfessor varchar(60) not null
	,celularProfessor varchar(9) not null
	,apelido varchar(25) not null
	,CONSTRAINT pkProfessor primary key(IDProfessor)
	,CONSTRAINT uqEmailProf unique(emailProfessor)
	,CONSTRAINT uqCelProf unique(celularProfessor)
	,CONSTRAINT fkUserInProfessor foreign key(IDUser) references Usuario(IDUser)
)
CREATE TABLE Disciplina (
	IDDisciplina int identity (1,1) 
	,nome varchar (20) not null
	,data_disciplina datetime not null
	,status_disciplina varchar(20) not null
	,plano_de_ensino varchar(50) not null
	,carga_horaria int not null
	,competencias varchar(50) not null
	,habilidades varchar (50) not null
	,ementa varchar(50) not null
	,conteudo_programatico varchar(100) not null
	,bibliografia_basica varchar (100) not null
	,bibliografia_complementar varchar(200) not null
	,percentual_pratico decimal(2,2) not null 
	,percentual_teorico decimal(2,2) not null
	,IDCoordenador int not null
	,CONSTRAINT pkDisciplina primary key (IDDisciplina)
	,CONSTRAINT fkIDCoordenadorInDisciplina foreign key(IDCoordenador) references Coordenador(IDCoordenador)
	,CONSTRAINT CHK_Disciplina_P_P CHECK (percentual_pratico>=0 or percentual_pratico<= 100)
	,CONSTRAINT CHK_Disciplina_P_T CHECK (percentual_teorico>=0 or percentual_teorico<= 100)
	,CONSTRAINT CHK_Disciplina_C_H CHECK (carga_horaria<= 200)
	,CONSTRAINT CHK_Disciplina_S CHECK(status_disciplina='ativo' or status_disciplina='inativo')
)
CREATE TABLE Curso(
	IDCurso int identity(1,1)
	,nome varchar(20) not null
	,CONSTRAINT pkCurso primary key (IDCurso)
	,CONSTRAINT uqNomeCurso unique(nome)
	
)
CREATE TABLE DisciplinaOfertada(
	IDDisciplinaOfertada int identity(1,1)
	,dt_inicio_matricula date
	,dt_fim_matricula date 
	,ano date not null
	,semestre smallint not null
	,turma varchar(20) not null
	,metodologia varchar(20)
	,recursos varchar (20)
	,criterio_avaliacao varchar (20)
	,plano_de_aulas varchar(20)
	,IDDisciplina int not null
	,IDProfessor int
	,IDCoordenador int not null
	,IDCurso int not null
	,CONSTRAINT pkDisciplinaOfertada primary key(IDDisciplinaOfertada)
	,CONSTRAINT CHK_DisciplinaOf_Ano CHECK (ano>='1900/01/01' or ano <='2100/01/01')
	,CONSTRAINT CHK_DisciplinaOf_Semestre CHECK (semestre >= 1 or semestre <=2)
	,CONSTRAINT CHK_DisciplinaOf_Turma CHECK (turma<=26)
	,CONSTRAINT fkIDDisciplinaInDiscOfert foreign key(IDDisciplina ) references Disciplina(IDDisciplina )
	,CONSTRAINT fkIDProfessorInDiscOfert foreign key(IDProfessor) references Professor(IDProfessor)
	,CONSTRAINT fkIDCoordenadorInDiscOfert foreign key(IDCoordenador) references coordenador(IDCoordenador)
	,CONSTRAINT fkIDCursoInDiscOfert foreign key(IDCurso) references Curso(IDCurso)

)
CREATE TABLE SolicitacaoMatricula(
	IDSolicitacaoMatricula int identity (1,1)
	,DtSolicitacao date default GETDATE()  not null
	,status_matricula varchar(20) default 'Solicitada'
	,IDCoordenador int
	,IDAluno int not null
	,IDDisciplinaOfertada int not null
	,CONSTRAINT pkSolicitacaoMatricula primary key(IDSolicitacaoMatricula)
	,CONSTRAINT fkIDCoordenadorInSolicitMatr foreign key(IDCoordenador) references Coordenador(IDCoordenador)
	,CONSTRAINT fkIDAlunoInSolicitMatr foreign key(IDAluno) references Aluno(IDAluno)
	,CONSTRAINT CHK_Matricula_Status CHECK (status_matricula='Solicitada'or status_matricula='Aprovada' or status_matricula='Rejeitada' or status_matricula='Cancelada' )
	,CONSTRAINT fkIDDisciplinaOfertadaInSolicitMatr foreign key(IDDisciplinaOfertada) references DisciplinaOfertada(IDDisciplinaOfertada)
)
CREATE TABLE Atividade(
	IDAtividade int identity(1,1)
	,titulo varchar(15) not null
	,descricao varchar(50) 
	,conteudo varchar(50) not null
	,tipo_atividade varchar(20) default 'Aberta' not null
	,atividades_extras varchar(50)
	,IDProfessor int not null
	,CONSTRAINT pkAtividade primary key (IDAtividade)
	,CONSTRAINT fkIDProfessorInAtividade foreign key(IDProfessor) references Professor(IDProfessor) 
	,CONSTRAINT CHK_Tipo_Atividade CHECK (tipo_atividade='Resposta'or tipo_atividade='Teste')
	,CONSTRAINT uqTituloAtiv UNIQUE (titulo)
)
CREATE TABLE AtividadeVinculada(
	IDAtividadeVinculada int identity (1,1)
	,rotulo varchar(50) not null
	,status_atividade_vinculada varchar(100) not null
	,dtInicioRespotas date not null
	,dtFimRespostas date not null
	,IDProfessor int not null
	,IDDisciplinaOfertada int not null
	,IDAtividade int not null
	,CONSTRAINT pkAtividadeVinculada primary key (IDAtividadeVinculada)
	,CONSTRAINT fkIDProfessorInAtivVinc foreign key(IdProfessor) references Professor(IDProfessor)
	,CONSTRAINT fkDisciplinaOfertadaInAtivVinc foreign key(IDDisciplinaOfertada) references DisciplinaOfertada(IDDisciplinaOfertada)
	,CONSTRAINT fkAtividadeInAtivVinc foreign key (IDAtividade) references Atividade(IDAtividade)
)
CREATE TABLE Entrega(
	IDEntrega int identity (1,1)
	,titulo varchar(20) not null
	,resposta varchar(100) not null
	,dtEntrega datetime default GETDATE() not null
	,dtAvaliacao date 
	,status_entrega varchar(20) default 'Entregue' not null
	,IDAtividadeVinculada int not null
	,IDAluno int not null
	,IDProfessor int
	,nota float
	,obs varchar(50)
	,CONSTRAINT pkEntrega primary key(IDEntrega)
	,CONSTRAINT fkIDAlunoInEntrega foreign key(IDAluno) references Aluno(IDAluno)
	,CONSTRAINT fkAtividadeVincInEntrega foreign key (IDAtividadeVinculada) references AtividadeVinculada(IDAtividadeVinculada)
	,CONSTRAINT fkIDProfessorInEntrega foreign key(IdProfessor) references Professor(IDProfessor)
	,CONSTRAINT CHK_nota CHECK(nota>=0.00 or nota <=10.00)
)
CREATE TABLE Mensagem (
	IDMensagem int identity (1,1)
	,assunto varchar(50)not null
	,referencia varchar(50)not null 
	,conteudo varchar(50)not null
	,status_mensagem varchar(25) default 'Enviado'not null
	,dtEnvio date default GETDATE()not null
	,dtResposta date
	,resposta varchar(100)
	,IDProfessor int not null
	,IDAluno int not null
	,CONSTRAINT fkIDProfessorInMensagem foreign key(IDProfessor) references Professor(IDProfessor)
	,CONSTRAINT fkIDAlunoInMensagem foreign key(IDAluno) references Aluno(IDAluno)
	,CONSTRAINT pkMensagem primary key (IDMensagem)

)