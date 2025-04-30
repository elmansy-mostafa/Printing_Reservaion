import pandas as pd
from io import BytesIO
from fastapi.responses import StreamingResponse

def export_to_excel(reservations):
    df = pd.DataFrame(reservations)
    excel_file = BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)
    return StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=reservations.xlsx"})
