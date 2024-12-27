import flet as ft

def main(page: ft.Page):
  page.title = "Lista de Tarefas"

  lista_tarefas = ft.ListView()

  def adicionar_tarefa(e):
    tarefa = txt_tarefa.value
    lista_tarefas.controls.append(
      ft.Container(
        ft.Text(tarefa),
        bgcolor=ft.colors.GREY_200,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
        margin=ft.margin.only(bottom=10),
        border_radius=ft.border_radius.all(5),
      )
    )
    page.update()
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    
  txt_titulo = ft.Text("Lista de Tarefas", size=24, weight=ft.FontWeight.BOLD)  
  txt_tarefa = ft.TextField(label="Nova Tarefa")
  add_tarefa = ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa)

  page.add(
    txt_titulo,
    txt_tarefa,
    add_tarefa,
    lista_tarefas,
  )

ft.app(target=main)