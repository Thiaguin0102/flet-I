import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    tarefa_input = ft.TextField(label="Nova Tarefa", width=300)
    add_button = ft.ElevatedButton("Adicionar", on_click=lambda e: add_tarefa())
    tarefa_lista = ft.Column()
    
    def add_tarefa():
        tarefa_text = tarefa_input.value
        if tarefa_text:
            tarefa_lista.controls.append(ft.Text(tarefa_text))
            tarefa_input.value = ""  # Limpa o campo de entrada
            tarefa_input.focus()  # Retorna o foco ao campo de entrada
            page.update()  # Atualiza a página

    page.add(tarefa_input, add_button, tarefa_lista)


ft.app(target=main)
