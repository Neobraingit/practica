
from datetime import time
from datetime import datetime

hora_actual = datetime(2023, 11, 12, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
hora_a_comparar = datetime(2023, 11, 15)
print (hora_actual - hora_a_comparar)