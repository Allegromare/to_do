import flet as ft

def main(page strat): ft.Page):
    page.title = "Tasker"
    
    # Initialize tasks in-memory list
    tasks = []
    
    # Create list view to display tasks
    task_list = ft.ListView(expand=True, spacing=10)
    
    # Create task input controls
    new_task = ft.TextField(hint_text="Enter task name", expand=True)
    
    def add_task(e):
        """Add new task to the list"""
        if new_task.value:
            task = new_task.value
            new_task.value = ""
            
            # Create checkbox with task name
            chk = ft.Checkbox(label=task, value=False)
            tasks.append(chk)
            
            # Add checkbox to list view
            task_list.controls.append(chk)
            page.update()
    
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Row(
                        controls=[new_task, ft.FilledButton("Add", on_click=add_task)],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    task_list
                ]
            )
        )
    )

ft run(main)
