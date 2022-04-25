from celery import shared_task
import pandas as pd

import datetime
from account.models import User
from company.models import Holding, Komanda, Ofis, Shirket, Shobe, Vezifeler
from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    OfisGunler,
    ShirketGunler,
    ShobeGunler,
    VezifeGunler
)

# Isci gunler ---------------------------------------------------
@shared_task(name='work_day_creater_task1')
def work_day_creater_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    users = User.objects.all()
    print(f"users ==> {users}")

    for user in users:
        isci_gunler = IsciGunler.objects.filter(
            isci = user,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery isci_gunler ==> {isci_gunler}")
        if len(isci_gunler) != 0:
            continue
        else:
            isci_gunler = IsciGunler.objects.create(
                isci = user,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            isci_gunler.save()


@shared_task(name='work_day_creater_task15')
def work_day_creater_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    users = User.objects.all()
    print(f"users ==> {users}")

    for user in users:
        isci_gunler = IsciGunler.objects.filter(
            isci = user,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery isci_gunler ==> {isci_gunler}")
        if len(isci_gunler) != 0:
            continue
        else:
            isci_gunler = IsciGunler.objects.create(
                isci = user,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            isci_gunler.save()

# Holding gunler ---------------------------------------------------
@shared_task(name='work_day_creater_holding_task1')
def work_day_creater_holding_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    holdings = Holding.objects.all()
    print(f"holdings ==> {holdings}")

    for holding in holdings:
        holding_gunler = HoldingGunler.objects.filter(
            holding = holding,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery holding_gunler ==> {holding_gunler}")
        if len(holding_gunler) != 0:
            continue
        else:
            holding_gunler = HoldingGunler.objects.create(
                holding = holding,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            holding_gunler.save()

@shared_task(name='work_day_creater_holding_task15')
def work_day_creater_holding_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    holdings = Holding.objects.all()
    print(f"holdings ==> {holdings}")

    for holding in holdings:
        holding_gunler = HoldingGunler.objects.filter(
            holding = holding,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery holding_gunler ==> {holding_gunler}")
        if len(holding_gunler) != 0:
            continue
        else:
            holding_gunler = HoldingGunler.objects.create(
                holding = holding,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            holding_gunler.save()

# Shirket gunler ---------------------------------------------------
@shared_task(name='work_day_creater_shirket_task1')
def work_day_creater_shirket_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    shirketler = Shirket.objects.all()
    print(f"shirketler ==> {shirketler}")

    for shirket in shirketler:
        shirket_gunler = ShirketGunler.objects.filter(
            shirket = shirket,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery shirket_gunler ==> {shirket_gunler}")
        if len(shirket_gunler) != 0:
            continue
        else:
            shirket_gunler = ShirketGunler.objects.create(
                shirket = shirket,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            shirket_gunler.save()

@shared_task(name='work_day_creater_shirket_task15')
def work_day_creater_shirket_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    shirketler = Shirket.objects.all()
    print(f"shirketler ==> {shirketler}")

    for shirket in shirketler:
        shirket_gunler = ShirketGunler.objects.filter(
            shirket = shirket,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery shirket_gunler ==> {shirket_gunler}")
        if len(shirket_gunler) != 0:
            continue
        else:
            shirket_gunler = ShirketGunler.objects.create(
                shirket = shirket,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            shirket_gunler.save()


# Ofis gunler ---------------------------------------------------
@shared_task(name='work_day_creater_ofis_task1')
def work_day_creater_ofis_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    ofisler = Ofis.objects.all()
    print(f"ofisler ==> {ofisler}")

    for ofis in ofisler:
        ofis_gunler = OfisGunler.objects.filter(
            ofis = ofis,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery ofis_gunler ==> {ofis_gunler}")
        if len(ofis_gunler) != 0:
            continue
        else:
            ofis_gunler = OfisGunler.objects.create(
                ofis = ofis,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            ofis_gunler.save()

@shared_task(name='work_day_creater_ofis_task15')
def work_day_creater_ofis_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    ofisler = Ofis.objects.all()
    print(f"ofisler ==> {ofisler}")

    for ofis in ofisler:
        ofis_gunler = OfisGunler.objects.filter(
            ofis = ofis,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery ofis_gunler ==> {ofis_gunler}")
        if len(ofis_gunler) != 0:
            continue
        else:
            ofis_gunler = OfisGunler.objects.create(
                ofis = ofis,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            ofis_gunler.save()

# Shobe gunler ---------------------------------------------------
@shared_task(name='work_day_creater_shobe_task1')
def work_day_creater_shobe_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    shobeler = Shobe.objects.all()
    print(f"shobeler ==> {shobeler}")

    for shobe in shobeler:
        shobe_gunler = ShobeGunler.objects.filter(
            shobe = shobe,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery shobe_gunler ==> {shobe_gunler}")
        if len(shobe_gunler) != 0:
            continue
        else:
            shobe_gunler = ShobeGunler.objects.create(
                shobe = shobe,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            shobe_gunler.save()

@shared_task(name='work_day_creater_shobe_task15')
def work_day_creater_shobe_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    shobeler = Shobe.objects.all()
    print(f"shobeler ==> {shobeler}")

    for shobe in shobeler:
        shobe_gunler = ShobeGunler.objects.filter(
            shobe = shobe,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery shobe_gunler ==> {shobe_gunler}")
        if len(shobe_gunler) != 0:
            continue
        else:
            shobe_gunler = ShobeGunler.objects.create(
                shobe = shobe,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            shobe_gunler.save()


# Komanda gunler ---------------------------------------------------
@shared_task(name='work_day_creater_komanda_task1')
def work_day_creater_komanda_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    komandalar = Komanda.objects.all()
    print(f"komandalar ==> {komandalar}")

    vezife = Vezifeler.objects.all()
    print(f"vezife ==> {vezife}")

    for komanda in komandalar:
        komanda_gunler = KomandaGunler.objects.filter(
            komanda = komanda,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery komanda_gunler ==> {komanda_gunler}")
        if len(komanda_gunler) != 0:
            continue
        else:
            komanda_gunler = KomandaGunler.objects.create(
                komanda = komanda,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            komanda_gunler.save()

@shared_task(name='work_day_creater_komanda_task15')
def work_day_creater_komanda_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    komandalar = Komanda.objects.all()
    print(f"komandalar ==> {komandalar}")

    for komanda in komandalar:
        komanda_gunler = KomandaGunler.objects.filter(
            komanda = komanda,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery komanda_gunler ==> {komanda_gunler}")
        if len(komanda_gunler) != 0:
            continue
        else:
            komanda_gunler = KomandaGunler.objects.create(
                komanda = komanda,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            komanda_gunler.save()


# Vezife gunler ---------------------------------------------------
@shared_task(name='work_day_creater_vezife_task1')
def work_day_creater_vezife_task1():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    vezifeler = Vezifeler.objects.all()
    print(f"vezifeler ==> {vezifeler}")

    for vezife in vezifeler:
        vezife_gunler = VezifeGunler.objects.filter(
            vezife = vezife,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery vezife_gunler ==> {vezife_gunler}")
        if len(vezife_gunler) != 0:
            continue
        else:
            vezife_gunler = VezifeGunler.objects.create(
                vezife = vezife,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            vezife_gunler.save()

@shared_task(name='work_day_creater_vezife_task15')
def work_day_creater_vezife_task15():
    """
    İş və tətil günlərini create edən task
    """
    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    vezifeler = Vezifeler.objects.all()
    print(f"vezifeler ==> {vezifeler}")

    for vezife in vezifeler:
        vezife_gunler = VezifeGunler.objects.filter(
            vezife = vezife,
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery vezife_gunler ==> {vezife_gunler}")
        if len(vezife_gunler) != 0:
            continue
        else:
            vezife_gunler = VezifeGunler.objects.create(
                vezife = vezife,
                is_gunleri_count=days_in_mont,
                tarix = f"{next_m.year}-{next_m.month}-{1}"
            )
            vezife_gunler.save()