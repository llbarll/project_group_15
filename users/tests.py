from django.test import TestCase
from users.forms import RegistrationForm
from django.forms import ValidationError
from users.models import Customer
# Create your tests here.
class RegistrationTests (TestCase):
    def setUp(self):
        Customer.objects.create(username='123456780') 
    
    def test_validate_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number':'123456789'}
        result = form.clean_id_number()
        self.assertEqual(result, '123456789')
        
    def test_reject_invalid_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number':'12345678a'}
        self.assertRaises(ValidationError,form.clean_id_number)
    
    def test_reject_duplicate_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number':'123456780'}
        self.assertRaises(ValidationError,form.clean_id_number)    
        
    def test_validate_secretary_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number':'12345678M'}
        result = form.clean_id_number()
        self.assertEqual(result, '12345678M')
        
    def test_validate_phone_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'phone_number':'1549357633'}
        result = form.clean_phone_number()
        self.assertEqual(result, '1549357633')
    
    def test_reject_invalid_phone_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'phone_number':'154935763a'}
        self.assertRaises(ValidationError,form.clean_phone_number)  
    
    
    
    def test_validate_first_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'first_name':'tamar'}
        result = form.clean_first_name()
        self.assertEqual(result, 'tamar')
    
    def test_reject_invalid_first_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'first_name':'tamar1'}
        self.assertRaises(ValidationError,form.clean_first_name) 
    
    def test_validate_last_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'last_name':'cohen'}
        result = form.clean_last_name()
        self.assertEqual(result, 'cohen')
    
    def test_reject_invalid_last_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'last_name':'cohen1'}
        self.assertRaises(ValidationError,form.clean_last_name)
    