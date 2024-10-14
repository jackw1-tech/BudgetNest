from decimal import Decimal
from django.conf import settings
from Users.models import Utente
from .models import Conto, IntestazioniConto, SaldoTotale, TipoConto, SaldoTotaleInvestimenti, PosizioneAperta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
class AccountService:
    def get_conti(primary_key):
        return Conto.objects.get(pk=primary_key)

    def get_intestazioni(pk):
        return IntestazioniConto.objects.filter(utente=pk)
    
    def get_conti_utente(pk):
        intestazioni = AccountService.get_intestazioni(pk)
        lista_conti = [] 
        for conto_intestato in intestazioni:
                conto = AccountService.get_conti(conto_intestato.conto.pk)
                lista_conti.append(conto)
        return lista_conti
    
    def get_conti_investimento_utente(pk):
        intestazioni = AccountService.get_intestazioni(pk)
        lista_conti = [] 
        for conto_intestato in intestazioni:
                conto = Conto.objects.filter(pk=conto_intestato.conto.pk, tipo= TipoConto.INVESTIMENTO)
                for c in conto:
                    lista_conti.append(c)
        return lista_conti
    
    
    def get_family_members(famiglia):
        family_members = Utente.objects.filter(famiglia=famiglia)
        return family_members

    
    def get_family_accounts(famiglia):
      
        family_members = Utente.objects.filter(famiglia=famiglia)
       
        accounts = IntestazioniConto.objects.filter(utente__in=family_members)

        
        accounts_grouped = accounts.values('conto').annotate(num_utenti=Count('utente'))
        
        
        # Filtra solo i conti che hanno intestazioni per tutti i membri della famiglia
        accounts_with_all_members = accounts_grouped.filter(num_utenti=len(family_members))
       
        
        
        final_accounts = Conto.objects.filter(pk__in=accounts_with_all_members.values('conto')).distinct()
   
        return list(final_accounts)
    
  

    def calcola_saldo_totale(utente):
    
        conti = AccountService.get_conti_utente(utente)
        totale = sum(conto.saldo for conto in conti)  # Calcola il saldo totale

        # Controlla se esiste già un SaldoTotale per l'utente con la data di oggi
        data_aggiornamento = timezone.now().date()
        try:
            saldo = SaldoTotale.objects.get(utente=utente, data_aggiornamento=data_aggiornamento)
            saldo.saldo_totale = totale
            saldo.save()
             # Puoi anche gestire questa situazione come preferisci
        except ObjectDoesNotExist:
            # Se non esiste, crea un nuovo oggetto SaldoTotale
            SaldoTotale.objects.create(
                utente=utente,
                saldo_totale=totale,  # Assicurati che il campo si chiami 'saldo_totale'
                data_aggiornamento=data_aggiornamento
            )
            print("Nuovo saldo totale creato.")

        
    def modifica_saldo_totale(utente, transazione):
        riga_saldo = SaldoTotale.objects.get(utente = utente, data_aggiornamento = timezone.now().date() )  
        riga_saldo.saldo_totale += transazione
        riga_saldo.save()


    def calcola_saldo_totale_investimenti(utente):
        conti = AccountService.get_conti_investimento_utente(utente)
        totale = sum(conto.saldo for conto in conti)  
        data_aggiornamento = timezone.now().date()
        try:
            saldo = SaldoTotaleInvestimenti.objects.get(utente=utente, data_aggiornamento=data_aggiornamento)
            saldo.saldo_totale = totale
            saldo.save()
             # Puoi anche gestire questa situazione come preferisci
        except ObjectDoesNotExist:
            # Se non esiste, crea un nuovo oggetto SaldoTotale
            SaldoTotaleInvestimenti.objects.create(
                utente=utente,
                saldo_totale=totale,  # Assicurati che il campo si chiami 'saldo_totale'
                data_aggiornamento=data_aggiornamento
            )
            print("Nuovo saldo totale creato.")
    
    
        
    def modifica_saldo_totale_investimenti(utente, transazione):
        riga_saldo = SaldoTotaleInvestimenti.objects.get(utente = utente, data_aggiornamento = timezone.now().date() )  
        riga_saldo.saldo_totale += transazione
        riga_saldo.save()


    def get_posizioni(utente):
        p = PosizioneAperta.objects.filter(utente = utente)
        return p
        
    def calcola_pmc(posizione):
        posizione.pmc = posizione.saldo_investito / posizione.numero_azioni
        posizione.save()
        return
    
        
   
    def registra_posizione_investimento(utente, conto, ticker, numero_azioni, prezzo_azione, nome_azienda):
        
        posizioni = AccountService.get_posizioni(utente= utente)
        
        for posizione in posizioni:
            if(posizione.conto == conto and posizione.utente == utente and posizione.ticker == ticker):
                posizione.numero_azioni += Decimal(numero_azioni)
                posizione.saldo_investito += Decimal(numero_azioni*prezzo_azione)
                posizione.saldo_totale += Decimal(numero_azioni*prezzo_azione)
                posizione.save()
                AccountService.calcola_pmc(posizione)
                return
       
        PosizioneAperta.objects.create(
            utente = utente,
            saldo_totale = (numero_azioni*prezzo_azione),
            saldo_investito = (numero_azioni*prezzo_azione),
            pmc = prezzo_azione,
            differenza = 0,
            ticker = ticker,
            nome_azienda = nome_azienda,
            conto = conto,
            numero_azioni = numero_azioni
            )
        return

