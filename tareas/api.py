from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Tarea

api = NinjaAPI(title="API de Tareas con Django Ninja")

# Schemas de validación de datos (Pydantic)
class TareaIn(Schema):
    titulo: str

class TareaOut(Schema):
    id: int
    titulo: str
    completada: bool

# Endpoints
@api.get("/tareas", response=List[TareaOut])
def listar_tareas(request):
    return Tarea.objects.all()

@api.post("/tareas", response=TareaOut)
def crear_tarea(request, payload: TareaIn):
    tarea = Tarea.objects.create(**payload.dict())
    return tarea

@api.patch("/tareas/{tarea_id}/completar", response=TareaOut)
def completar_tarea(request, tarea_id: int):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.save()
    return tarea