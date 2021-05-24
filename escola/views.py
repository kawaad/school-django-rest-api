from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, \
                              ListaMatriculaAlunoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os alunos e alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as matrículas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaAluno(generics.ListAPIView):
    '''Exibindo as matrículas de um aluno ou aluna'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer