# services.py
from .models import Utente,Famiglia  # Importa il tuo modello

class UserService:
    def get_all_utente():
      return Utente.objects.all()
    
    def get_all_Famiglia():
      return Utente.objects.all()
       
    def count_utenti():
        return Utente.objects.count()  
    
    def count_famiglie():
        return Famiglia.objects.count() 