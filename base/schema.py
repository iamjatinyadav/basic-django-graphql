import graphene
from graphene_django import DjangoObjectType

from .models import *


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "age")

class CreateStudent(graphene.Mutation):
  class Arguments:
    name = graphene.String()
    age = graphene.Int()

  ok = graphene.Boolean()
  student = graphene.Field(StudentType)

  def mutate(self, info, name, age):
    student = Student(name=name, age=age)
    student.save()
    return CreateStudent(ok=True, student=student )


class DeleteStudent(graphene.Mutation):
  class Arguments:
    id = graphene.Int()

  ok = graphene.Boolean()

  def mutate(self, info, id):
    student = Student.objects.get(id=id)
    student.delete()
    return DeleteStudent(ok=True)


class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        age = graphene.Int()
    ok= graphene.Boolean()
    student = graphene.Field(StudentType)

    def mutate(self, info, id, name, age):
        student = Student.objects.get(id=id)
        student.name = name
        student.age = age
        student.save()
        return UpdateStudent(ok=True, student = student)


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    one_student = graphene.Field(StudentType, id =graphene.Int())

    def resolve_all_students(root, info):
        return Student.objects.all()

    def resolve_one_student(root, info, id):
        return Student.objects.get(id=id)


class Mutation(graphene.ObjectType):
  create_student = CreateStudent.Field()
  delete_student = DeleteStudent.Field()
  update_student = UpdateStudent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)