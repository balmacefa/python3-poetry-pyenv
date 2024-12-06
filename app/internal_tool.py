from pywebio.input import input_group, file_upload, textarea, input, actions
from pywebio.output import  put_column, put_table, put_buttons, put_text, clear, toast
from pywebio.platform.fastapi import webio_routes
from pywebio import start_server


# Función principal de la herramienta
def internal_tool_pdf_reader():
    rows = []  # Lista de filas dinámicas
    pdf_file = None

    def render_table():
        """Renderiza la tabla dinámica en la interfaz"""
        clear()  # Limpia la pantalla
        table_content = [["Condition", "Redacción", "Acciones"]]
        
        for idx, row in enumerate(rows):
            table_content.append([
                input(f"Condition-{idx+1}", value=row["condition"]),
                textarea(f"Redacción-{idx+1}", value=row["textarea"]),
                put_buttons([
                    {"label": "Eliminar", "value": idx, "color": "danger"},
                    {"label": "Arriba", "value": f"up-{idx}", "color": "info"},
                    {"label": "Abajo", "value": f"down-{idx}", "color": "info"}
                ], onclick=lambda x: handle_row_action(x, idx))
            ])
        
        put_column([
            put_table(table_content),
            put_buttons([
                {"label": "Agregar Fila", "value": "add_row", "color": "success"},
                {"label": "Cargar PDF", "value": "upload_pdf", "color": "primary"},
                {"label": "Iniciar Proceso", "value": "start_process", "color": "success"},
            ], onclick=handle_action)
        ])

    def handle_row_action(action, idx):
        """Maneja las acciones de las filas (eliminar, subir, bajar)"""
        nonlocal rows
        if action == idx:  # Eliminar
            rows.pop(idx)
        elif action == f"up-{idx}" and idx > 0:  # Subir
            rows[idx], rows[idx-1] = rows[idx-1], rows[idx]
        elif action == f"down-{idx}" and idx < len(rows) - 1:  # Bajar
            rows[idx], rows[idx+1] = rows[idx+1], rows[idx]
        render_table()

    def handle_action(action):
        """Maneja las acciones principales"""
        nonlocal pdf_file
        if action == "add_row":  # Agregar fila
            rows.append({"condition": "", "textarea": ""})
        elif action == "upload_pdf":  # Subir PDF
            pdf_file = file_upload("Sube un archivo PDF", accept=".pdf")
            toast("Archivo PDF cargado exitosamente", color="success")
        elif action == "start_process":  # Iniciar proceso
            if pdf_file is None:
                toast("Por favor, sube un archivo PDF antes de iniciar el proceso", color="error")
                return
            toast("¡Proceso iniciado!", color="success")
        render_table()

    render_table()

