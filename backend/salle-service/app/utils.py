def check_availability(salle_id):
    from .models import Salle
    salle = Salle.query.get(salle_id)
    return salle.available if salle else False

def update_availability(salle_id, available):
    from .models import Salle
    salle = Salle.query.get(salle_id)
    if salle:
        salle.available = available
        db.session.commit()