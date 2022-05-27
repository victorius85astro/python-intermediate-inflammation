"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_patient():
    from inflammation.models import Patient
    name = 'Viktor'
    p = Patient(name=name)
    assert p.name == name


def test_no_duplicate_patients():
    from inflammation.models import Doctor, Patient
    doc = Doctor("Viktor")
    patient = Patient("Pera")
    doc.add_patient(patient)
    doc.add_patient(patient)
    assert len(doc.patients) == 1


