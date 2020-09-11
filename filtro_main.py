import pandas as pd
import alumno_obj as al

def __check_survey(survey):
	for k,v in survey.items():
	    print(f'**Alumno id {k+1}** | Profesor: {v.respuestas[7]}')
	    print(v.respuestas)
	    print(' ')
	    print('-----'*5)
	    print(' ')

def _generar_survey(diagnostico_df, preguntas, respuestas):
	i = 0
	dir_alumnos = {}

	while i < len(diagnostico_df):
	    alumno = al.Alumno(i+1, preguntas, respuestas[i])
	    dir_alumnos[i] = alumno
	    i += 1

	return dir_alumnos

def _generar_preguntas(diagnostico_df):
	return list(diagnostico_df)

def _generar_respuestas(diagnostico_df):
	respuestas = []
	i = 0 #Indice contador
	while i < len(diagnostico_df):
		respuestas.append(list(diagnostico_df.iloc[i]))
		i += 1

	return respuestas


def main(diagnostico_df):
	preguntas = _generar_preguntas(diagnostico_df)
	respuestas = _generar_respuestas(diagnostico_df)
	survey = _generar_survey(diagnostico_df, preguntas,respuestas)
	__check_survey(survey)

if __name__ == '__main__':
	diagnostico_df = pd.read_csv('Diagnostico_oficial - Hoja 1.csv')
	main(diagnostico_df)	 